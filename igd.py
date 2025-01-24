import requests

def igd(in_link, user, admin_username):
    print(in_link)
    url = f'https://tele-social.vercel.app/down?url={in_link}'
    response = requests.get(url).json()
    print(response)

    # Extract video details from the response
    video_data = response.get('data', {})
    video_url = video_data.get('video', '')

    if not video_url:
        return None, "Sorry, we couldn't find the video. Please try again later."

    return video_url