import requests
from datetime import timedelta, datetime
import time
import json
from convert_json import ConvertJson

class ScrapeGithub:

    def get_links(params, token, page):
        url = f'https://api.github.com/search/repositories?q={params}&per_page=100&page={page}'
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github+json'
        }
        print(url)
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None

    def create_json_line(params, token, page, total_count):
        total = 0
        link_list = []
        with open('/product/app/data/input_link_list.json', 'a') as github_search_json:
            while total < total_count:
                page += 1
                response = ScrapeGithub.get_links(params, token, page)
                if not response:
                    break
                data = response.json()
                repositories = data['items']
                rate_limit = response.headers.get('X-RateLimit-Remaining')
                if repositories:
                    for repo in enumerate(repositories):
                        link = json.dumps({'link': repo[1]['html_url']})
                        link_list.append(link)
                        github_search_json.write(link + ',\n')
                        total += 1
                else:
                    if rate_limit == '1':
                        print("Reached rate limit, waiting...")
                        time.sleep(50)  
                    break
                if rate_limit == '1':
                    print("Reached rate limit, waiting...")
                    time.sleep(50)

    def organize_params(phrase, token, total_count,start_date_str, finish_date_str):
        page = 0
        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
            finish_date = datetime.strptime(finish_date_str, '%Y-%m-%d') if finish_date_str else datetime.today()
            if not finish_date_str:
                finish_date = datetime.today()
            while start_date < finish_date:
                start_date += timedelta(days=1)
                date = start_date.strftime("%Y-%m-%d")
                print(date)
                params = f'created:{date}+{phrase}'
                ScrapeGithub.create_json_line(params, token, page, total_count)
                page = 0
        else:
            params = phrase
            ScrapeGithub.create_json_line(params, token, page, total_count)

    def check_and_search(phrase, token,start_date_str, finish_date_str):
        response = requests.get(f'https://api.github.com/search/repositories?q={phrase}&per_page=100&page=1').json()
        total_count = response['total_count']
        if total_count and not start_date_str:
            print('Your search has more than 1000 results. To get all results you have to define a start and a finish date')
        ScrapeGithub.organize_params(phrase, token, total_count,start_date_str, finish_date_str) 
        ConvertJson.convert_json()