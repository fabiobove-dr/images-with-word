import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from src.ImageWithWord import ImageWithWord


def main():
     
    # create an instance of the ImageWithWord class with default font name and size
    image_with_word = ImageWithWord(word='Hello', font_size=24)

    # save the image to a file
    image_with_word.save_image('word_image.png')

if __name__ == "__main__":
    main()