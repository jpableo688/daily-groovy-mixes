# Daily Groovy Mixes w/ Scraping (TwitterBot)
- This Python program features a automated tweeting bot that will tweet each song in a SoundCloud playlist daily (or in a specified time unit).
- Great use for those wanting to spread music tastes and advertising music/mixes on your Twitter feed.
- Playlists will need to be made public for this Twitter Bot to work.
-  __Developer Note:__ Once SoundCloud continues to hand out developer API credentials (currently unavailable due to high volume of requests), scraping for the link to the songs will not be needed, making playlists private will be possible as well.

## Usage
- Host locally or on a python cloud host service. 
- Run:

  ```python3 main.py```

## How This Works
- Using the Twitter API credentials that you will provide yourself, you will be able to tweet songs on SoundCloud using the SoundCloud widget on Twitter.
- The mule to this project would be ```scraper.py```. Should any issues arise, it would be advisable to check there first. ```scraper.py``` sends a GET request to the SoundCloud link to get the HTML of the page of the playlist. By observing the ```section``` tag in the HTML, notice that all the songs in the playlist are there as well along with the URL. Simply just parse the HTML to get the URL. The ```return_link()``` function will do this for you and check if you have used that song already, which is stored in the ```used_links``` file. If the link has been used then skip to the next link in the playlist. This function will return a full SoundCloud link which you will be able to tweet directly on Twitter triggering the SoundCloud widget.
- The other classes such as ```twitter.py``` will contain the API credentials for Twitter and simply formats the SoundCloud link into a presentable tweet. The ```main.py``` file controls the sleep timer which will wake every 24 hours at a certain time to tweet your "Daily Groovy Mix".

## Dependencies
### Using PIP:
- Tweepy
- BeautifulSoup
- requests
