from twitterscraper.query import get_proxies
import requests

def get_categories():
    response = requests.get('https://twitter.com/i/api/graphql/gIlavFaiRvOlXdmXaQX9Uw/TopicsPickerPage?variables=%7B%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Atrue%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D',
        headers={
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'cookie': 'guest_id=v1%3A164814513329110254; gt=1507056039551713284; d_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMxSG71%252FAToMY3NyZl9p%250AZCIlMDFhNmNmNWUxMGZmNGUxOTAxZDIwNjBiYzBiNzg1NDQ6B2lkIiU1N2Ex%250AYjMwMDRiMjdjMThkNjNiY2M0Y2FlZjU1OTYzOQ%253D%253D--6e6e1192df1921404f441facc9610340aea4000c; g_state={"i_p":1648152359083,"i_l":1}; kdt=K6qfeodGic82Ln4TaGhxa2o35fOKqTDKjxuyyoxV; auth_token=0e502696b92023810c9ff8ce590480833b0fb4a8; ct0=4e7a870f4c71568a0a22bf9df1468ebaccd4f4424a972e162dc9cf29acabc3c996548a4c9c5e07223ec4fbe33c55376f3355004d80c76a30e064f07bfb5442297d84ac6b0154ad84f8f0c661eaf79668; twid=u%3D1462070018393481223; att=1-Pv6u0Y4er97pNSaDhsv93S36hEiHbo87qjjlSyqS',
            'x-csrf-token': '4e7a870f4c71568a0a22bf9df1468ebaccd4f4424a972e162dc9cf29acabc3c996548a4c9c5e07223ec4fbe33c55376f3355004d80c76a30e064f07bfb5442297d84ac6b0154ad84f8f0c661eaf79668',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en'
        }).json()
    instructions = response['data']['viewer']['topics_picker_page']['body']['timeline']['instructions']
    cat_set = set([])
    for i in instructions[2]['entries']:
        if i['content']['header']['text'] == 'Categories':
            # here are all the categories you are looking for:
            cat_set.union(set([(j['item']['itemContent']['content']['topic']['name'],j['item']['itemContent']['content']['topic']['topic_id']) for j in i['content']['items']]))
        if 'footer' in i['content']:
            cat_set.add((i['content']['header']['text'],i['content']['footer']['landingUrl']['url'].split('/')[-1]))
    for name, topic_id in cat_set:
        print(name)
    #requests.get(f'https://twitter.com/i/api/graphql/g_TMdZsyTj-_QutyL6io-g/TopicsPickerPageById?variables=%7B%22topicId%22%3A%{topic_id}%22%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Atrue%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D')
    #print(set(all_set)-cat_set)
    #items = response['data']['viewer']['topics_picker_page']['body']['timeline']['responseObjects']['feedbackActions']




if __name__ == "__main__":
    response = requests.get(
        'https://twitter.com/i/api/graphql/ouxBHylIc2FGh75gcdvK1g/TopicLandingPage?variables=%7B%22rest_id%22%3A%22898673391980261376%22%2C%22cursor%22%3A%22DAADCgABFOo05zR__-gPAAIKAAAAFBTodKzJl7AIFOkohAFUYAEU6PzvQFcgAhTof9XQWnAGFOhPEY7XEAMU6ZX40ZfQABTpiC_0l7ACFOicpe_VsAAU6CNFjNWABhTojQlvl9ADFOja0W3X0AwU6MEAEFogAhTnxcuvFxAIFOhGxgZUYAAU6K1auRRgAxTof13aFSABFOjxP7_XMAYU5-drYZcQAhTpmefnF9ACFOg9-LuaIAMAAA%22%2C%22context%22%3A%22%7B%7D%22%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Atrue%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D',
        headers={
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'cookie': 'guest_id=v1%3A164814513329110254; gt=1507056039551713284; d_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMxSG71%252FAToMY3NyZl9p%250AZCIlMDFhNmNmNWUxMGZmNGUxOTAxZDIwNjBiYzBiNzg1NDQ6B2lkIiU1N2Ex%250AYjMwMDRiMjdjMThkNjNiY2M0Y2FlZjU1OTYzOQ%253D%253D--6e6e1192df1921404f441facc9610340aea4000c; g_state={"i_p":1648152359083,"i_l":1}; kdt=K6qfeodGic82Ln4TaGhxa2o35fOKqTDKjxuyyoxV; auth_token=0e502696b92023810c9ff8ce590480833b0fb4a8; ct0=4e7a870f4c71568a0a22bf9df1468ebaccd4f4424a972e162dc9cf29acabc3c996548a4c9c5e07223ec4fbe33c55376f3355004d80c76a30e064f07bfb5442297d84ac6b0154ad84f8f0c661eaf79668; twid=u%3D1462070018393481223; att=1-Pv6u0Y4er97pNSaDhsv93S36hEiHbo87qjjlSyqS',
            'x-csrf-token': '4e7a870f4c71568a0a22bf9df1468ebaccd4f4424a972e162dc9cf29acabc3c996548a4c9c5e07223ec4fbe33c55376f3355004d80c76a30e064f07bfb5442297d84ac6b0154ad84f8f0c661eaf79668',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en'
        }).json()
    for entry in response['data']['topic_by_rest_id']['topic_page']['body']['timeline']['instructions'][0]['entries']:
        print(entry['entryId'])

        #for item in items:
        #name = item['value']['richBehavior']['topic']['name']
        #topic_id = item['value']['richBehavior']['topic']['topic_id']
        #if 'travel' in name.lower():
        #    print(name, topic_id)
