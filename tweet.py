import tweepy

 

def main():


    # Mettez vos clés d'api Twitter ici

    twitter_auth_keys = {

        "consumer_key"        : "XXXXXX",

        "consumer_secret"     : "XXXXXX",

        "access_token"        : "XXXXXX",

        "access_token_secret" : "XXXXXX"

    }

 

    auth = tweepy.OAuthHandler(

            twitter_auth_keys['consumer_key'],

            twitter_auth_keys['consumer_secret']

            )

    auth.set_access_token(

            twitter_auth_keys['access_token'],

            twitter_auth_keys['access_token_secret']

            )

    api = tweepy.API(auth)

 

    # Upload image

    media = api.media_upload("shop.jpg")

 

    # Post tweet with image

    tweet = "Boutique Fortnite d'aujourd'hui !\n\nN'oubliez pas d'activer les notifs pour ne ratez aucune boutique. 🔔\n\nVous pouvez également me soutenir en utilisant le code LamaEpik ! #ad"

    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    
    print('Tweet envoyé !')

 

if __name__ == "__main__":

    main()