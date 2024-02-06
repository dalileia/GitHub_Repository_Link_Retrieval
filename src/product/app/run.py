
from github_api import ScrapeGithub


if __name__ == '__main__':
    
    start_date = ''
    finish_date = ''
    phrase = 'search test api github'
    token = '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'

    ScrapeGithub.check_and_search(phrase,token,start_date,finish_date)
    
