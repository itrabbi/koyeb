import requests

def fb(fb_link):
    url = f'https://tele-social.vercel.app/down?url={fb_link}'
    response = requests.get(url).json()
    video_data = response['data'][0]
    video_url = video_data['url']  
    print("Video URL:", video_url) 
    if not video_url:
        return None, "Sorry, we couldn't find the video. Please try again later."

    return video_url