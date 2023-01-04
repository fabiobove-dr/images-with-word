"""
Before we start, it's important to note that you'll need to have a Facebook Developer account, and you'll need to apply for Instagram Basic Display API access. Once you have been approved, you'll receive an App ID and an App Secret, which you'll use to authenticate your API requests.
"""

import requests
from typing import Dict, List

class InstagramAPI:
    """
    A class for interacting with the Instagram Basic Display API.
    """
    def __init__(self, app_id: str, app_secret: str):
        """
        Initializes the InstagramAPI instance with the provided app ID and app secret.

        Parameters:
        - app_id (str): The app ID for your Instagram app.
        - app_secret (str): The app secret for your Instagram app.
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None

    def get_access_token(self, code: str) -> None:
        """
        Requests an access token from the Instagram API using the provided authorization code.

        Parameters:
        - code (str): The authorization code received from the authorization process.

        Returns:
        - None
        """
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

    def get_user_profile(self) -> Dict:
        """
        Requests the authenticated user's profile information from the Instagram API.

        Parameters:
        - None

        Returns:
        - A dictionary containing the user's profile information.
        """
        if not self.access_token:
            raise Exception("No access token set")
        url = "https://api.instagram.com/v1/users/self"
        params = {"access_token": self.access_token}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get user profile: {}".format(response.text))

    def post_image(self, image_path: str, description: str, hashtags: List[str]) -> None:
        """
        Posts an image to the authenticated user's Instagram feed.

        Parameters:
        - image_path (str): The path to the image file on the local filesystem.
        - description (str): The image's description.
        - hashtags (List[str]): A list of strings containing the hashtags to be used for the image.

        Returns:
        - None
        """
        if not self.access_token:
            raise Exception("No access token set")
        url = "https://api.instagram.com/v1/media/upload"
        files = {"image_file": open(image_path, "rb")}
        payload = {
            "access_token": self.access_token,
            "caption": "{}\n{}".format(description, " ".join(["#" + hashtag for hashtag in hashtags])),
        }
        response = requests.post(url, data=payload, files=files)
        if response.status_code != 200:
            raise Exception("Failed to post image: {}".format(response.text))
