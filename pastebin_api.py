"""
Library for interacting with the PasteBin API.
https://pastebin.com/doc_api
"""
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'LX73j-OWfmX462aF9sqIfhueryfJTFUv'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin.

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    api_dev_key = API_DEV_KEY
    url = PASTEBIN_API_POST_URL
    
    data = {
        'api_dev_key': api_dev_key,
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': '1' if not listed else '0',
        'api_option': 'paste'
    }

    print("Creating a new paste...")
    response = requests.post(url, data=data)

    # Print response details for debugging
    print("Response status code:", response.status_code)
    print("Response text:", response.text)

    if response.status_code == 200:
        print("Paste created successfully!")
        return response.text
    else:
        print(f"Failed to create paste. Response code: {response.status_code}")
        return None

# Example usage (uncomment to test)
if _name_ == '_main_':
    paste_url = post_new_paste("Test Title", "This is the body of the paste.", "10M", False)
    if paste_url:
        print(f"Paste URL: {paste_url}")
    else:
        print("Failed to create paste.")