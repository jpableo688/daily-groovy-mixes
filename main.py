from scraper import return_link
from twitter import template_tweet
from twitter import tweet
import time

first_run = True

def run_bot():
    url = return_link()
    to_tweet = ''

    if url != False:
        global first_run
        if first_run == True:
            first_run = False
            to_tweet = template_tweet(url)
            time.sleep(57060)
            tweet(to_tweet)
        else:
            to_tweet = template_tweet(url)
            tweet(to_tweet)

if __name__ == '__main__':
    while True:
        run_bot()
        time.sleep(86400)

