"""
Before we start, it's important to note that you'll need to have a Facebook Developer account, and you'll need to apply for Instagram Basic Display API access. Once you have been approved, you'll receive an App ID and an App Secret, which you'll use to authenticate your API requests.
"""

import requests

class InstagramAPI:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None

    def get_access_token(self, code):
        url = "https://api.instagram.com/oauth/access_token"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret,
            "grant_type": "authorization_code",
            "redirect_uri": "YOUR_REDIRECT_URI",
            "code": code
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
        else:
            raise Exception("Failed to get access token: {}".format(response.text))

    def get_user_profile(self):
        if not self.access_token:
            raise Exception("No access token set")
        url = "https://api.instagram.com/v1/users/self"
        params = {"access_token": self.access_token}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get user profile: {}".format(response.text))
