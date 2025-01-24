import requests

def yt(yt_link):
    url = f'https://tele-social.vercel.app/down?url={yt_link}'
    response = requests.get(url)
    data = response.json()
    video_url = data.get('video', '')
    video_title = data.get('title', 'Untitled Video')

    if not video_url:
        return None, "Sorry, we couldn't find the video. Please try again later."

    return video_url, video_title