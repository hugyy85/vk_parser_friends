import requests, json
from config import token


class VkApiUse:

    def __init__(self, user):
        self.user = user
        self.data = ''
        self.id = ''
        self.token = token

    # connectinon to vk API

    def connection(self):
        user_id = self.uid_to_id()
        f = requests.get(f'https://api.vk.com/method/friends.get?v=5.92&access_token={self.token}&user_id={user_id}&fields=country,city,contacts')
        data = json.loads(f.text)
        return data

    # rename nickname to id

    def uid_to_id(self):
        r = requests.get(f'https://api.vk.com/method/users.get?v=5.92&access_token={self.token}&user_ids={self.user}')
        data = json.loads(r.text)
        user_id = int(data['response'][0]['id'])
        return user_id

    # analysis of the information received

    def parse(self, data):
        result = {}

        try:
            for i in data['response']['items']:
                result[i['id']] = {
                    'first_name': i['first_name'],
                    'second_name': i['last_name'],
                    'country': i.get('country', {'title': 'None'}),
                    'city': i.get('city', {'title': 'None'}),
                    'mobile_phone': (i.get('mobile_phone')),
                    'home_phone': i.get('home_phone')
                }
        except KeyError:
            print(f'error in {data}')

        return result



