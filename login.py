import requests
from os import environ
import urllib.parse
import json

def main():
    '''
    session = requests.Session()
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}'
    }).json()
    guest_token = response['guest_token']

    response = session.post('https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login', headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
    }, json={
        "input_flow_data": {
            "flow_context": {
                "debug_overrides": {},
                "start_location": {
                    "location": "manual_link"
                }
            }
        },
        "subtask_versions": {
            "contacts_live_sync_permission_prompt": 0,
            "email_verification": 1,
            "topics_selector": 1,
            "wait_spinner": 1,
            "cta": 4
        }
    })

    print(response)
    #print(response.json())

    flow_token = response.json()['flow_token']
    username= "kierenfunk"

    response = session.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
    }, json={
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginJsInstrumentationSubtask",
                "js_instrumentation": {
                    #"response": "{\"rf\":{\"d793d703bc804d65ee2397fff3b75f112ba625c533e3668a822632d7c8586746\":-3,\"aefdbf03198a12f790853d828d6107e065df9051f4f788206bfb0fa532f63049\":-180,\"a286af073857975fe04fd70c7f85d3498fc3c6563bedb1cfb0556d818c7f0190\":-9,\"a70c85e409fdbe6f22792691bc63bbaa261f8dc5c646383ff55a2255d224d759\":-1},\"s\":\"c70BTrbKsQ-B7lq8_tjKbzMOooXeksqacVEEZamw-pqiKVhOYqgzEZHoE3rWwAWZyoiTonYRwdwBfXWn0Gr4X5gMyOwXJ0n2vIZDPH0NvmyPct6ZHKZg4lfb30KTGPdSX7wujLfs7pNfKHMjaoQfDFZuwnCtn-0FvFjqF1G8eH_WUel-w9lqR_aUdvwB5pIzl1wfoMKTNGShMNS-OFpJvbxal5P7-WyxXBTxO61j0xppsmyNENNecJq4_T4rUd3GjoXQcTv8fivKazAgxIJmOFf2j16ncRaY7bWtd2SagFEZnMguNndc31obCSf5jBUGtm4aN6ZqBQu38fuREVzQXgAAAYHOSOfo\"}",
                    "response": "{}",
                    "link": "next_link"
                }
            }
        ]
    })

    print(response)
    #print(response.json())
    flow_token = response.json()['flow_token']


    response = session.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
    }, json={
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginEnterUserIdentifierSSO",
                "settings_list": {
                    "setting_responses": [
                        {
                            "key": "user_identifier",
                            "response_data": {
                                "text_data": {
                                    "result": username
                                }
                            }
                        }
                    ],
                    "link": "next_link"
                }
            }
        ]
    })
    #print("\n"*2)
    print(response)
    flow_token = response.json()['flow_token']
    #print(json.dumps(response.json(), indent=2))
    #print(session.cookies.get_dict())
    #print("\n"*2)

    response = session.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
        'x-twitter-active-user': 'yes'
    }, json={
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginEnterPassword",
                "enter_password": {
                    "password": "VdlVQJ0oSMrSW7dxmXMvGNaET6sQmou296IZsCkhgeZD6vuGwX",
                    "link": "next_link"
                }
            }
        ]
    })


    #print("\n"*2)
    print(response)
    flow_token = response.json()['flow_token']
    #print(json.dumps(response.json(), indent=2))
    #print("\n"*2)
    response = session.post("https://twitter.com/i/api/1.1/onboarding/task.json", headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
    }, json={
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "AccountDuplicationCheck",
                "check_logged_in_account": {
                    "link": "AccountDuplicationCheck_false"
                }
            }
        ]
    })

    #print("\n"*2)
    print(response)
    #print(json.dumps(response.json(), indent=2))
    #print("\n"*2)

    print(guest_token)
    print(session.cookies.get_dict())
    '''

    guest_token = '1544323844567191552'
    cookies = {'auth_token': '1d485059e477d683c10720330dc9a5e796339727', 'ct0': 'a756836e75f61fb4b3b98718b5b7f3d8', 'guest_id': 'v1%3A165703047175748300', 'kdt': 'vTMhhgtkEDJQlPGbjBJTj9cluyVNmlYZkW8OEDy8', 'twid': '"u=1462070018393481223"'}


    response = requests.post("https://twitter.com/i/api/graphql/UCGeMTkwZnWkXUzzlHO8iw/HomeLatestTimeline", headers={
        'authorization': f'Bearer {environ.get("ACCESS_TOKEN")}',
        'x-guest-token': guest_token,
        #'x-csrf-token': session.cookies.get_dict()['ct0'],
        'x-csrf-token': cookies['ct0'],
        #'cookie': "; ".join([f"{key}={val}" for key,val in session.cookies.get_dict().items()])
        'cookie': "; ".join([f"{key}={val}" for key,val in cookies.items()])
    }, json={
        "variables": {
            #"count": 50,
            #"cursor": 'DAAJAAA',
            "includePromotedContent": False,
            "latestControlAvailable": True,
            "withSuperFollowsUserFields": True,
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True
        },
        "features": {
            "dont_mention_me_view_api_enabled": True,
            "interactive_text_enabled": True,
            "responsive_web_uc_gql_enabled": False,
            "vibe_tweet_context_enabled": False,
            "responsive_web_edit_tweet_api_enabled": False,
            "standardized_nudges_misinfo": False,
            "responsive_web_enhance_cards_enabled": False
        },
    })

    entries = [instruction for instruction in response.json()['data']['home']['home_timeline_urt']['instructions'] if instruction['type'] == 'TimelineAddEntries'][0]['entries']
    cursors = [entry for entry in entries if entry['content']['entryType'] == 'TimelineTimelineCursor']
    print(cursors)
    timeline_items = [entry['content'] for entry in entries if entry['content']['entryType'] == "TimelineTimelineItem"]# or entry['content']['entryType'] == "TimelineTimelineModule"]
    for item in reversed(timeline_items):
        if 'itemContent' in item:
            tweet = item['itemContent']['tweet_results']['result']
            user = tweet['core']['user_results']['result']['legacy']
            if 'retweeted_status_result' not in tweet['legacy']:
                #print(json.dumps(,indent=2))
                #print(tweet['legacy'])
                #print(tweet['core']['user_results']['result'])
                print(user['name'],f"@{user['screen_name']}",'   Followers:',user['followers_count'])
                print(tweet['legacy']['created_at'])
                print(tweet['legacy']['full_text'])
                print("-"*50+"\n")
                #print(json.dumps(tweet['legacy'], indent=2))
        #    print(entry['entryType'])
        #print(json.dumps(instructions,indent=2))
        #print(len(entries))
        else:
            print('*'*10+' MODULE '+'*'*10)
            for module_item in item['items']:
                tweet = module_item['item']['itemContent']['tweet_results']['result']
                user = tweet['core']['user_results']['result']['legacy']
                print('| \t'+user['name'],f"@{user['screen_name']}",'   Followers:',user['followers_count'])
                print('| \t'+tweet['legacy']['created_at'])
                print('| \t'+tweet['legacy']['full_text'])
                print("| \t")
            print("-"*50+"\n")
        

if __name__ == "__main__":
    main()
