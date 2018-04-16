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
userid='beauty_japan1'

followers_id=api.followers_ids(userid)#自分のアカウントのフォロワーを全て取得
following_id=api.friends_ids(userid)#自分のアカウントのフォロイングを全て取得する
for following in following_id:
    userfollowers=api.get_user(following).followers_count
    print('リムーブするユーザー名')
    username=api.get_user(following).name
    print(username)
    print('フォロワー数')
    print(userfollowers)
    api.destroy_friendship(following)
