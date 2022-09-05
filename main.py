import requests
from os import environ
import urllib.parse
import json

def main():

    session = requests.Session()
    response = session.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}'
    }).json()
    guest_token = response['guest_token']

    cursor = 'DAAJAAA'
    for i in range(10):
        variables = {
            "rest_id":environ.get("TOPIC_ID"),
            "cursor": cursor,
            "withSuperFollowsUserFields":True,
            "withDownvotePerspective":False,
            "withReactionsMetadata":False,
            "withReactionsPerspective":False,
            "withSuperFollowsTweetFields":True
        }
        features = {
            "dont_mention_me_view_api_enabled":True,
            "interactive_text_enabled":True,
            "responsive_web_uc_gql_enabled":False,
            "vibe_tweet_context_enabled":False,
            "responsive_web_edit_tweet_api_enabled":False,
            "standardized_nudges_misinfo":False,
            "responsive_web_enhance_cards_enabled":False
        }
        #example = 'variables=%7B%22rest_id%22%3A%22849075881653846016%22%2C%22cursor%22%3A%22DAADCgABFWclEn0__-YPAAIKAAAAFBVmgftC14AAFWV2L2wUsAAVZZbwNNZAARVlpgKJFbAAFWYB3KTWAAAVZamJvZqQABVmUe0D1xABFWV65hdWAAEVZRvjQlSwARVlkhXGl9ADFWWCn_sUYAAVZklFK9pAABVlemTJVRAAFWVeyuzaAAIVZZK_8tSwAhVliP741xACFWUdjYCXwAEVZYB6SxRgABVl0XAQV6AAFWYCnZhVUAEAAA%22%2C%22context%22%3A%22%7B%7D%22%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%7D&features=%7B%22dont_mention_me_view_api_enabled%22%3Atrue%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_uc_gql_enabled%22%3Afalse%2C%22vibe_tweet_context_enabled%22%3Afalse%2C%22responsive_web_edit_tweet_api_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'
        result = f'variables={urllib.parse.quote(json.dumps(variables).replace(" ", ""))}&features={urllib.parse.quote(json.dumps(features).replace(" ", ""))}'

        url = 'https://twitter.com/i/api/graphql/5tqVb5ewExoJpQdqhJwTqQ/TopicLandingPage?'+result

        response = session.get(url,
            headers={
                'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
                'x-guest-token': guest_token,
            }
        ).json()
        #print(response)
        timeline_entries = [instruction['entries'] for instruction in response['data']['topic_by_rest_id']['topic_page']['body']['timeline']['instructions'] if instruction['type'] == 'TimelineAddEntries'][0]
        for entry in timeline_entries:
            if entry['content']['entryType'] == 'TimelineTimelineCursor' and 'cursor-bottom' in entry['entryId']:
                cursor = entry['content']['value']
            #elif entry['content']['entryType'] == 'TimelineTimelineModule':
            elif entry['content']['entryType'] == 'TimelineTimelineItem':
                print(entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
                print("\n"+"-"*12)


if __name__ == "__main__":
    main()