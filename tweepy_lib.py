#tweepyライブラリをインポート
import tweepy
#各種キーをセット
CONSUMAR_KEY="oyH04vvcFdJccFDpNHigCwmVp"
CONSUMAR_SECRET="eIaNLZ80bt0j5GLfmScFOGsadfxUS8R0s9LM5t72enaguidxbm"
ACCESS_TOKEN="753782305995370496-XPBweSPkYrAzqYFThmluZn8f8Wcju82"
ACCESS_SECRET="AJ5xztwmcRFYNxQQyBEB2JiS1P1VYLJ8TB3S21iiV5rCY"
auth=tweepy.OAuthHandler(CONSUMAR_KEY,CONSUMAR_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
#APIインスタンスを作成
api=tweepy.API(auth)

q='AV女優'
count=100
search_results=api.search(q=q,count=count)

for result in search_results:
    username=result.user._json['screen_name']
    user_id=result.id #tweetのstatusオブジェクトからtweetidを取得
    print(user_id)
    user=result.user.name
    print(user)
    tweet=result.text
    print(tweet)
    time=result.created_at
    print(time)
    try:
        api.create_favorite(user_id)
        print(user)
        print('をライクしました')
        api.create_friendship(user_id)
        print('をフォローしました')
    except:
        print('すでにファボかフォロー済み')
    print('######################')
