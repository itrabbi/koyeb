import random
import requests

def nwaifu(chat_id, user, admin_username):
    # List of categories
    # categories = ["waifu", "neko", "trap"]
    categories = ["waifu"]
    
    # Randomly select a category
    category = random.choice(categories)
    
    # Construct the API URL
    url = f'https://api.waifu.pics/nsfw/{category}'
    
    # Make the request to the API
    response = requests.get(url).json()
    
    # Get the image URL from the response
    image_url = response.get('url')
    
    if not image_url:
        return {'image_url': None, 'caption': 'Error: No image found or invalid category.'}
    
    # Prepare the message content
    tele = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Random Nswf Waifu</b>\n
<b>↯ Category ⌁ {category}</b>
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b>
</strong>"""

    # Return the image URL and caption
    return {'image_url': image_url, 'caption': tele}
