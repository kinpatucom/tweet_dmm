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

#Tweet投稿用のURL
url="https://api.twitter.com/1.1/statuses/update.json"

#DMMのAPI ID,アフィリエイトID検索キーワードをセット

APPID='4qmCryP69RHCpxutP01c'
AFFILIATEID='kinpatucom-990'
KEYWORD='%E6%96%B0%E4%BA%BA%0A'

#DMMのAPIを取得しjsonをBeautifulSoupで取得
html=urllib.request.urlopen('https://api.dmm.com/affiliate/v3/ItemList?api_id='+APPID+'&affiliate_id='+AFFILIATEID+'&site=DMM.R18&service=digital&floor=videoa&hits=10&sort=date&keyword='+KEYWORD+'3&output=json')
soup=BeautifulSoup(html,'html5lib')

#取得したjsonを整理して表示
print('取得したデータを表示します')
print(soup.pretify())

#タイトル、女優、画像URL、動画URLを追加
items=soup.items
print('取得したitems数:{}'.format(len(items.item)))
for item in items:
    print('----------------')
    title=item.title.string #動画タイトル
    title=(title[:40]+'..動画はコチラ→')　if len(title) > 75 else title #タイトルが40字を超えたら省略
    print('title:{}'.format(title))
    photoURL=item.imageurl.large.string #画像URL
    print('photoURL:{}'.format(photoURL))

    #動画によってはサンプルがない。ない場合エラーになるのでtryで囲む
    try:
        videoURL=item.samplemovieurl.size_476_360.string
        print('videoURL:{}'.format(videoURL))
        #Tweet内容
        content=title + '|' + videoURL
        print('Tweet内容:{}'.format(content))

        #DMMから取得した画像を一度ローカルに保存
        request=request.get(photoURL,stream=True)
        filename='temp.jpg'
        if request.status_code == 200:
            print('status_code==200')
            with open(filename,'wb') as image:
                for chunk in request:
                    image.write(chunk)
            api.update_with_media(filename,status=content)
            print('Tweetに成功しました')
            os.remove(filename)
        else:
            print('画像をダウンロードできませんでした')
    except Exception as e:
        print(e)
print('プログラムを終了しました')
