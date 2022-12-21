import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from src.ImageWithWordBuilder import ImageWithWordBuilder


def main():
    image_with_word = ImageWithWordBuilder(
        image_size=None, 
        font_family=None, 
        font_size=None, 
        word="Prova", 
        file_name=None
    )
   

if __name__ == "__main__":
    main()