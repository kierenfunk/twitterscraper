import requests
import json
from bs4 import BeautifulSoup


def test_twitter():
    session = requests.Session()
    response = session.get('https://twitter.com/search')
    soup = BeautifulSoup(response.text, 'html.parser')
    guest_token = ''
    for script in soup.find_all('script'):
        if script.text.startswith('window.__INITIAL_STATE__='):
            body = json.loads(script.text[len('window.__INITIAL_STATE__='):script.text.index('window.__META_DATA__')-1])
            guest_token = body['session']['guestId']

    response = session.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    },data={
        'guest_token': guest_token
    })
    guest_token = response.json()['guest_token']

    response = session.get('https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=python%20min_replies%3A5%20lang%3Aen%20-filter%3Areplies&tweet_search_mode=live&count=20&query_source=typed_query&cursor=scroll%3AthGAVUV0VFVBaAwL2RgoueyioWiMC90db0wcsqEnEV4IJ6FYCJehgEVVNFUjUBFQIVAAA%3D&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo', headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': guest_token
    })
    for tweet_id,tweet in response.json()['globalObjects']['tweets'].items():
        #print('\n')
        #print(tweet_id)
        print(tweet['created_at'])
        #print(tweet['full_text'])
