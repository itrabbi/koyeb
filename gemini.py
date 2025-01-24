import requests
import json

# Gemini API URL (replace with your actual endpoint)
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDLhfGGtMCkg8njCx_Sc6WzZn0Py1bkUsU"

def gem(gem, id, usertele):
    headers = {
        "Content-Type": "application/json"
    }
    # Construct the request payload based on the gem argument
    data = {
            "contents": [
                {
                    "parts": [
                        {"text": gem}
                    ]
                }
            ]
        }

    # Send the request to the Gemini API
    response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Parse the response JSON
        response_data = response.json()

        # Extract the AI-generated content with error handling
        try:
            ai_response_text = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No response text found.')
        except (KeyError, IndexError):
            ai_response_text = "Error: Could not parse response."

        # Create the custom Telegram message
        tele = f"""<b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Gemini.Ai</b>\n
<b>↯ Response ⌁</b> {ai_response_text}
<b>↯ ReqBy ⌁ @{usertele}</b>
<b>↯ DevBy ⌁ @rabbisudo</b>
"""

        return tele
    else:
        # Handle unsuccessful API request
        return f"Error: API request failed with status code {response.status_code}. Response text: {response.text}"