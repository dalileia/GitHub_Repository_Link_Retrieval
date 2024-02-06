
from github_api import ScrapeGithub


if __name__ == '__main__':
    
    #Date: YYYY-MM-DD
    start_date = ''
    finish_date = ''
    phrase = 'search test api github'
    token = ''

    ScrapeGithub.check_and_search(phrase,token,start_date,finish_date)
    
