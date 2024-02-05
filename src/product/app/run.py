
from github_api import ScrapeGithub


if __name__ == '__main__':
    
    start_date = ''
    finish_date = ''
    phrase = 'search test'
    token = ''

    ScrapeGithub.check_search(phrase,token,start_date,finish_date)
    
