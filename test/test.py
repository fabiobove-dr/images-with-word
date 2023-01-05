import sys
import time
import yaml
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from src.ImageWithWord import ImageWithWord
from src.InstaConnect import InstagramAPI

# Load the oauth_settings.yml file
stream          = open('../oauth.yml', 'r')
settings        = yaml.load(stream, yaml.SafeLoader)
app_id          = settings['app_id']
app_secret      = settings['app_secret']
token_client      = settings['short_lived_access_token']

def main():
     
    # create an instance of the ImageWithWord class with default font name and size
    image_with_word = ImageWithWord(word='Hello', font_size=24)

    # save the image to a file
    file_name = time.time()
    image_with_word.save_image(f'../images/{file_name}.png')

    instagram_api = InstagramAPI(app_id, app_secret)
    instagram_api.exchange_token(token_client)
    instagram_api.post_image("../images/test.png", "This is my image!", ["#cool", "#fun"])
    
if __name__ == "__main__":
    main()