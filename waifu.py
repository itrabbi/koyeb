import requests

def waifu(chat_id, user,admin_username):
    # Get the random waifu image from waifu.pics
    url = 'https://api.waifu.pics/sfw/waifu'
    response = requests.get(url).json()
    image_url = response.get('url')
    
    # Prepare the message content
    tele = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Random Waifu</b>\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b>
</strong>"""

    # Return the image URL and caption
    return {'image_url': image_url, 'caption': tele}