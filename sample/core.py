from time import sleep
from selene import config
from selene.browsers import BrowserName
from selene.api import *

from selenium import webdriver

BLEAGUE_SCHEDULE_URL = 'https://www.bleague.jp/schedule/'

def main():
    try:
        config.browser_name = BrowserName.CHROME
        browser.open_url(get_bleague_schedule_url(year=2016))
        s('dt.dtFirst').click()
        sleep(2)
    except:
        raise

def get_bleague_schedule_url(tab=1, year=2018, event=1, club='', setuFrom=1, setuTo=1):
    return BLEAGUE_SCHEDULE_URL + '?tab=' + str(tab) + '&year=' + str(year) + '&event=' + str(event)\
            + '&club=' + str(club) + '&setuFrom=' + str(setuFrom) + '&setuTo=' + str(setuTo)

if __name__ == '__main__':
    main()
