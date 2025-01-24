import requests

def pi(pi_link, user, admin_username):
    url = f'https://yoogo-vip.vercel.app/fetch_media?link={pi_link}'
    response = requests.get(url).json()
    image_url = response.get('url')

    tele = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Pinterest Downloader</b>\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b>
</strong>"""

    return {'image_url': image_url, 'caption': tele}