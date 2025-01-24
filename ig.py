import requests
from json import *


def igg(usernameig,user,admin_username):
    print(usernameig,user,admin_username)
    he = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar",
        "cookie": "csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-asbd-id": "198387",
        "x-csrftoken": "qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
    }
    urlg = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={usernameig}"
    try:
        re = requests.get(urlg, headers=he).json()
        print(re)
        bio = re["data"]["user"]["biography"]
        followers = re["data"]["user"]["edge_followed_by"]["count"]
        following = re["data"]["user"]["edge_follow"]["count"]
        name = re["data"]["user"]["full_name"]
        iid = re["data"]["user"]["id"]
        img = re["data"]["user"]["profile_pic_url_hd"]
        posts = re["data"]["user"]["edge_owner_to_timeline_media"]["count"]
        return f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot" rel="noopener noreferrer">YooGo↯</a> ⌁ Instagram Information</b>\n
↯ NAME ⌁ <code>{name}</code>
↯ ID ⌁ <code>{iid}</code>
↯ Followers ⌁ {followers}
↯ Following ⌁ {following}
↯ Bio ⌁ <code>{bio}</code>
↯ Posts ⌁ {posts}
↯ Profile Pic ⌁ <a href="{img}">Click View</a>\n\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b>
        </strong>"""
    except requests.exceptions.RequestException as e:
        return "Error"