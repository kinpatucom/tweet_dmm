import urllib.request
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
from TweetAPI import TwitterAPI
import request
import tweepy
import os

#各種キーをセット
CONSUMAR_KEY="oyH04vvcFdJccFDpNHigCwmVp"
CONSUMAR_SECRET="eIaNLZ80bt0j5GLfmScFOGsadfxUS8R0s9LM5t72enaguidxbm"
ACCESS_TOKEN="753782305995370496-XPBweSPkYrAzqYFThmluZn8f8Wcju82"
ACCESS_SECRET="AJ5xztwmcRFYNxQQyBEB2JiS1P1VYLJ8TB3S21iiV5rCY"

#apiを取得
auth=tweepy.OAuthHandler(CONSUMAR_KEY,CONSUMAR_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api=tweepy.API(auth)

#twitterないを検索し結果をエクセルに書き込む
for status in api.search(q='',lang='ja',result_type='recent',count=100):
    status.user.name #useridが出てくる
    status.user.screen_name #ユーザー名が出てくる
    status.text #Tweet内容が出てくる
    status.created_at + datetime.timedelta(hours=),format #投稿時間が出てくる
    
