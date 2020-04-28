# SimpleTweetScraper
A simple scraper for getting tweets with timestamps from a given user.

## What you Need:
  Python
  Pip
  Twitter API Credentials
    - Unless you have these the API won't let you in. But rest assured, they are pretty easy to get. You can request a 'Developer Account' here: https://developer.twitter.com/en/docs/basics/developer-portal/overview. Usually they'll get back to you in about a week.
 
#=============================================== Super Basic Scraping! ========================================

## Instructions

1. Open up your terminal and CD to a folder where you'll want to save CSV files of scraped tweets. I made one called 'scrapedtweets'. Easy.

2. In terminal, type in python and hit enter to boot up python within that folder.

3. Copy and paste the code in tweepy.py INTO A TEXT EDITOR of some kind (Sublime, Atom, etc.)

4. Once there, find where it says 'users' at the bottom of the code. This is a python list that the program will go through, scraping tweets for each user in the list. So, if you had this: users = ['bob','sally','dennisrodman'] the program would run once for each of those users, bob, sally and dennisrodman.

5. Once you've filled in your users, copy and paste everything into the Python terminal you opened up.

6. Press enter. When the three '>>>' return, your code is finished running. Check your folder contents to see the tweets you scraped. It should look like bob.csv, sally.csv, dennisrodman.csv. **

7. That's it. That's the scrape.

####### If you do this to fast, or copy and paste extra symbols, the python might not run and give you an error. Try copy and pasting a couple times before you begin to debug. This happens to me often.

#========================================= Next Level, Personalized Scraping!=================================

Once you've figured that out, you should play with the parameters in the code. You can change the code to get different tweets. For example, you can get more tweets if you change the 'count' parameter. And, you can include retweets if you set include_rts to 'true'. 

And you can change the way it writes to your csv, if you need those tweets in a different order.

To do that, you need to know some basic python. I recommend going to this site http://socialdata.site/ where one of the data professors at the CUNY Newmark School of Journalism has actually written a book on how to scrape from sites like Youtube, Wikipedia, etc. Very user-friendly. It uses Python.

If you have any questions about this scraper, you can email me at luca.powell@journalism.cuny.edu.

Happy scraping,
Luca
