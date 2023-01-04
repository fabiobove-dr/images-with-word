from PIL import Image, ImageDraw, ImageFont

class ImageWithWord:
    DEFAULT_FONT_NAME = 'arial'
    DEFAULT_FONT_SIZE = 36

    def __init__(self, word: str, font_name: str = DEFAULT_FONT_NAME, font_size: int = DEFAULT_FONT_SIZE):
        """Initialize the ImageWithWord instance with the given word, font name, and font size.
        
        Args:
            word (str): The word to display in the image.
            font_name (str, optional): The name of the font to use. Defaults to 'arial'.
            font_size (int, optional): The size of the font to use. Defaults to 36.
        """
        self.word = word
        self.font_name = font_name
        self.font_size = font_size

        self.validate_word()
        self.validate_font_name()
        self.validate_font_size()

    def validate_word(self):
        """Validate the word parameter."""
        if not self.word:
            raise ValueError('word cannot be empty')

    def validate_font_name(self):
        """Validate the font_name parameter."""
        if not self.font_name:
            raise ValueError('font_name cannot be empty')

        try:
            ImageFont.truetype(self.font_name, 10)
        except OSError:
            raise ValueError('font_name is not a valid font')

    def validate_font_size(self):
        """Validate the font_size parameter."""
        if self.font_size <= 0:
            raise ValueError('font_size must be a positive integer')

    def create_image(self) -> Image:
        """Create an image with the specified word, font name, and font size.
        
        Returns:
            Image: An instance of the Image class with the specified word drawn in the middle.
        """
        # create a blank image with a white background
        image = Image.new('RGB', (200, 50), color = 'white')

        # get a drawing context
        draw = ImageDraw.Draw(image)

        # choose a font
        font = ImageFont.truetype(self.font_name, self.font_size)

        # draw the word in the middle of the image
        draw.text((100 - self.font_size, 25 - self.font_size), self.word, font=font, fill='black')

        return image

    def save_image(self, file_name: str):
        """Save the image to a file.
        
        Args:
            file_name (str): The name of the file to save the image to.
        """
        # generate the image
        image = self.create_image()

        # save the image to a file
        image.save(file_name)


