"""
This class implements the integration with Mastadon's profiles.
The idea is to simulate victim's activity that communicates to a 
Mastadon fake profile.
"""
import requests
import json

def get_profile(profile_handler):
    return json.loads(requests.get(f'https://mas.to/api/v1/accounts/lookup?acct={profile_handler}').text)


profiles_file = open('knock_knock/mastodon_profiles.txt', 'r')
malicious_urls_file = json.load(open('knockknock/malicious_urls.json', 'r'))
for profile in profiles_file.readlines():
    try:
        urls = get_profile(profile)['note'].replace('<p>','').replace('</p>','').replace('hello','').strip().split('|')
        for url in urls:
            if url:
                if url not in malicious_urls_file:
                    print(f'Adding new URL: {url}')
                    malicious_urls_file[url] = [profile.strip()]
                else:
                    if profile not in malicious_urls_file[url]:
                        malicious_urls_file[url].append(profile.strip())
    except KeyError:
        continue

json.dump(malicious_urls_file, open('knock_knock/malicious_urls.json', 'w'), indent=True)

        
            
        

