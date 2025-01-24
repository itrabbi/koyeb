import requests

def tik(tik_link):
    url = f'https://tele-social.vercel.app/down?url={tik_link}'
    response = requests.get(url).json()
    # Extract video details from the response
    video_data = response.get('data', {})
    video_url = video_data.get('video', '')
    if not video_url:
        return None, "Sorry, we couldn't find the video. Please try again later."

    return video_url