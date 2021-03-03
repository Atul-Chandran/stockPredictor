#Google API installation
# get_ipython().system('pip install pytrends')
import random as r
import time
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
from nsetools import Nse
nse=Nse()
from pytrends.request import TrendReq
#Google API declaration
pytrends = TrendReq(hl='en-US', tz=360)

kw_list=[]
file=open('Companies.txt','r')
lines=file.readlines()
for line in lines:
    time.sleep(10)
    kw_list.append(line.rstrip())
# kw_list=["Infosys","Wipro","HDFC","DMART","Accenture"]

count=[]
print("Started")
num=r.randint(1,5)*r.randint(1,5)
print("Time for next API call is ",num)
#time.sleep(num)
#count=pytrends.build_payload(kw_list, cat=0, timeframe='today 3-h', geo='', gprop='')
count=pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, year_end=2018, month_end=2, day_end=1, cat=0, geo='', gprop='', sleep=num)
count=count.drop(['isPartial'],axis=1)
datasum=[]
searchValues=[]


i=0
sum1=0

for i in range(len(kw_list)):
    datasum.append(list(count[kw_list[i]].values.tolist()))
    searchValues.append(sum(datasum[i]))
index=0    
largestValue=searchValues[0]
for i in range(len(searchValues)):
    if searchValues[i]>largestValue:
        largestValue=searchValues[i]
        index=i
    else:
        pass

###############





# get_ipython().system('pip install matplotlib')
access_token="1274889426-5JJDwoMkSRfY9CnjdM9b0YcMJiyVidRl5ywlJ4s"
access_token_secret="fmwcoaffGXNW9eZ4TSbz0ZSlzKZucD7dm8kbjOiMNViSG"
consumer_key="SMrRB5lvwvQmnuga00aY3DaLN"
consumer_secret="0RwndwaNNcOO1dPh0rPd6rR2berHVllzPxyHEI3Ib0QLCAVG4H"
import tweepy #The Twitter API
#from Tkinter import * #For the GUI
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
#print (user.name)
public_tweets = api.home_timeline()
# get_ipython().system('pip install quandl')

import matplotlib.pyplot as plt
# get_ipython().system('pip install mpl-finance')
# get_ipython().system('pip install googlefinance')
from mpl_finance import candlestick_ohlc

import matplotlib.dates as mdates
#import candlestick_ohlc

import pandas as pd
#from matplotlib.finance import candlestick_ohlc
#import pandas_datareader
#!pip install pandas-datareader.data as web

#!pip install matplotlib
#from matplotlib import finance

# get_ipython().system('pip install pandas_datareader ')
from pandas_datareader import data as web

#!pip install googlefinance.get
#from googlefinance.get 

# get_ipython().system('pip install beautifulsoup4')
# get_ipython().system('pip install scikit-learn')
import datetime as dt
from matplotlib import style

style.use('ggplot');
start=dt.datetime(2019,6,1);
end=dt.datetime(2019,6,13);

#########
iterVar=1;

#companies=['INFY.BO','JUBLFOOD.BO','BOROSIL.BO','HDFC.NS','DMART.BO'];
comp=[];
file=open('Companies.txt','r');
lines=file.readlines();
for line in lines:
    comp.append(line);
    
company=[];
for line in comp:
    company.append(''.join(comp));
    



print("***************************************\n\n")
print("Fetching stock prices from ",len(comp)," companies\n");
print("***************************************\n\n");

#print("Type of companies is ",type(companies[1])," and Type of company is ",type(company[1]))


print("\n\nCompanies are\n");
for a in range(len(comp)):
    if '.' in comp[a].rstrip():
        print(comp[a].rstrip()[0:-3]+",",end=" ");
    else:
        print(comp[a].rstrip()+",",end=" ");


        
#print("One of the companies is ",company[1], " and ",companies[1]);
#########
count=1;
#var=companies[iterVar];
variable=[]

for a in range(len(comp)):
    tweetSentiment=0;
    
    name=comp[a].rstrip();
    
       
    infy=web.DataReader(comp[a].rstrip(),'yahoo',start,end);
    infy.to_csv('CSV/'+name+'.csv');

    infy.plot();
    infy['Company '+'%d' %(count)]=infy['Adj Close'].rolling(window=1,min_periods=1).mean();
    variable.append(infy['Company '+'%d' %(count)].tail(1))
    #print("\nPrinting company ",count," ",infy['Company '+'%d' %(count)])
    infy.dropna(inplace=True);
    infy_ohlc=infy['Adj Close'].resample('1D').ohlc();
    infy_volume=infy['Volume'].resample('1D').sum();

    infy_ohlc.reset_index(inplace=True);
    infy_ohlc['Date']=infy_ohlc['Date'].map(mdates.date2num);

    print("\n\n------","(",count,")" ,comp[a].rstrip(),"------\n\n\n\n")
    print("\nPrinting the Open High Low Close");
    print(infy_ohlc.head());
    print(infy.head());
    infy_ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1);
    infy_ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=infy_ax1);
    infy_ax1.plot(infy.index,infy['Adj Close']);
    infy_ax1.set_title(comp[a]);
    infy_ax1.xaxis_date();
    candlestick_ohlc(infy_ax1,infy_ohlc.values,width=2,colorup='R');

    infy_ax1.plot(infy.index,infy['Company '+'%d' %(count)]);

    infy_ax2.fill_between(infy_volume.index.map(mdates.date2num),infy_volume.values,0);
    plt.show()

    print("Tweets regarding ",name," are\n\n")        
    print("************\n\n")
    tweetCount = 5
# Creating the API object while passing in auth information
    api = tweepy.API(auth)

# The search term you want to find
    query = ["Stock",name]
#query1="Market"
# Language code (follows ISO 639-1 standards)
    language = "en"
# Calling the user_timeline function with our parameters
    results=api.search(id=name,q=query, lang=language,count=tweetCount)
# foreach through all tweets pulled
    for tweet in results:
   # printing the text stored inside the tweet object
       if tweet.created_at>start:
           print(tweet.user.screen_name,"Tweeted:",tweet.text)
           tweetSentiment=analyser.polarity_scores(tweet.text)['pos']+analyser.polarity_scores(tweet.text)['neu']
 
        
    count=count+1
    print("\n The tweets positivity are ",(tweetSentiment/tweetCount)*100,"%");
    if((tweetSentiment)*100)>1:
        print("\n\n ",name,"'s stock is most likely going to improve")
    else:
        print("\n\n ",name,"'s stock might decline gradually")

count=0;
print("According to the data from Google API, ",kw_list[index]," will have the highest stock value among the given list of companies")

while(count<len(comp)):
    print("\n\n",comp[count].rstrip(),"'s predicted stock price is ",variable[count]);
    count=count+1;

# count=0
# file=open('Companies.txt','r');
# line=file.readlines();
# while count<len(line):
#     print(line[count]);
#     count=count+1;
