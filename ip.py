import requests

def ip(ip_address, id, user):
    ip_url = f"https://api.ipgeolocation.io/ipgeo?apiKey=f9ac4c270c8c475aa84ffd2ec6ee9871&ip={ip_address}"
    response = requests.get(ip_url)
    ip_details = response.json()

     # Extract relevant details from the JSON response
    ip_address = ip_details.get('ip', 'unknown')
    country_name = ip_details.get('country_name', 'unknown')
    continent_name = ip_details.get('continent_name', 'unknown')
    country_emoji = ip_details.get('country_emoji', 'unknown')
    city = ip_details.get('city', 'unknown')
    zipcode = ip_details.get('zipcode', 'unknown')
    isp = ip_details.get('isp', 'unknown')
    organization = ip_details.get('organization', 'unknown')
    latitude = ip_details.get('latitude', 'unknown')
    longitude = ip_details.get('longitude', 'unknown')
    timezone = ip_details.get('time_zone', {}).get('name', 'unknown')
    currency_code = ip_details.get('currency', {}).get('code', 'unknown')

        # Create the custom Telegram message
    tele = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ IP Information</b>\n
↯ IP Address ⌁ <code>{ip_address}</code>
↯ Continent ⌁ <code>{continent_name}</code>
↯ Country ⌁ <code>{country_name} {country_emoji}</code>
↯ City ⌁ <code>{city}</code>
↯ Zip Code ⌁ <code>{zipcode}</code>
↯ Location ⌁ <code>{latitude},{longitude}</code>
↯ ISP ⌁ <code>{isp}</code>
↯ Organization ⌁ <code>{organization}</code>
↯ Timezone ⌁ <code>{timezone}</code>
↯ Currency ⌁ <code>{currency_code}</code>\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ @rabbisudo</b>
</strong>"""
    return tele