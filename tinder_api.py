import requests
from time import sleep
import random
import json

host = 'https://api.gotinder.com'
#leave tinder_token empty if you don't use phone verification
tinder_token = 'tinder_token_api'
headers = {'X-Auth-Token':tinder_token, 
        'Content-Type':'application/json', 
        'User-Agent':'Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)'}

# tinder search preferences
age_filter_min = 18
gender_filter = 1 # 1 for female, 0 for male
gender = 0
age_filter_max = 30
distance_filter = 1

def get_recommendations():
    url = host + '/user/recs'
    recommendations = requests.get(url, headers=headers)
    return recommendations

def modify_position(lat, lon):
    url = host + '/user/ping'
    data = '{"lat":"%s", "lon":"%s"}' % (lat, lon)
    new_position = requests.post(url, data=data, headers=headers)
    if new_position.status_code == 200:
        return True
    else:
        return False

def set_profile_pref():
    url = host + '/profile'
    data = '{"age_filter_min": "%s", "gender_filter": "%s", "gender": "%s", "age_filter_max": "%s", "distance_filter": "%s"}' \
            % (age_filter_min, gender_filter, gender, age_filter_max, distance_filter)
    profile_pref = requests.post(url, data=data, headers=headers)
    if profile_pref.status_code == 200:
        return True
    else:
        return False


research_locations = [{'id': 1, 'coordinates': [48.03346454286551, -0.76909]},
 {'id': 2, 'coordinates': [48.0199736366485, -0.7574805424396046]},
 {'id': 3, 'coordinates': [48.0199736366485, -0.7806994575603955]},
 {'id': 4, 'coordinates': [48.03526324974078, -0.76909]},
 {'id': 5, 'coordinates': [48.01907402278517, -0.7551588932787766]},
 {'id': 6, 'coordinates': [48.01907402278517, -0.7830211067212235]},
 {'id': 7, 'coordinates': [48.0370619560501, -0.76909]},
 {'id': 8, 'coordinates': [48.0181743618647, -0.7528373248990338]},
 {'id': 9, 'coordinates': [48.0181743618647, -0.7853426751009663]},
 {'id': 10, 'coordinates': [48.03886066179351, -0.76909]},
 {'id': 11, 'coordinates': [48.01727465389018, -0.7505158372992363]},
 {'id': 12, 'coordinates': [48.01727465389018, -0.7876641627007638]},
 {'id': 13, 'coordinates': [48.04065936697097, -0.76909]},
 {'id': 14, 'coordinates': [48.016374898864704, -0.748194430478213]},
 {'id': 15, 'coordinates': [48.016374898864704, -0.7899855695217871]},
 {'id': 16, 'coordinates': [48.04245807158251, -0.76909]},
 {'id': 17, 'coordinates': [48.01547509679137, -0.7458731044348531]},
 {'id': 18, 'coordinates': [48.01547509679137, -0.792306895565147]}]

for l in research_locations:
    print(set_profile_pref())
    print(modify_position(l['coordinates'][0],l['coordinates'][1]))
    data = get_recommendations().json()
    print(data)
    with open('data/rec_'+str(l['id'])+'.json', 'w') as f:
        json.dump(data, f)
    sleep(random.randint(600,1200))

