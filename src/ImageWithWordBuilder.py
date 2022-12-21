from PIL import Image, ImageDraw, ImageFont
import time

class ImageWithWordBuilder:
	def __init__(self, image_size: float, font_family: str, font_size: float, word:str, file_name: str):

		# Image attributes: size
		self.minimum_image_size 	= 100
		self.default_image_size 	= 300 
		self.image_size 			= self.set_image_size(image_size)	

		# Font attributes: size, color and family
		self.minimum_font_size  	= 8
		self.default_font_size 		= 12
		self.default_font_family 	= 'arial.ttf'
		self.font_family 			= self.set_font(font_family, font_size)
		self.txt_color				= "black"
		
		self.word					= self.set_word(word)
		self.file_name 				= self.set_filename(file_name)
		self.image 					= None

	def set_filename(self, file_name: str):
		self.file_name = f"{str(time.time)}.JPEG" if file_name is None else file_name

	def set_word(self, word):
		self.word ="ETAOIN SHRDLU" if word is None else word

	def get_word(self):
		return self.word 

	def set_image_size(self, image_size: float) -> None:
		"""
		"""
		print('Setting image size...')
		if image_size is None or image_size < 100:
			print(f'Invalid image size, image size value set as default: {self.default_image_size}')
			self.image_size = self.default_image_size
		else:
			print(f'Image size set to: {image_size}')
			self.image_size = image_size   

	def set_font(self, font_family: str, font_size: float) -> None:
		"""
		"""
		print('Setting font...')
		if font_size < self.minimum_font_size or font_size is None:
			print(f'Invalid font size, font size set to default value: {self.default_font_size}')
			font_size = self.default_font_size
		if font_family is None:
			print(f'Invalid font family, font family set to default value: {self.default_font_family}')
			font_family = self.default_font_family
		print(f'Font set: {font_family, font_size}')
		self.font = ImageFont.truetype(font_family, font_size)

	def draw_text_on_img(self):
		"""Draw a text on an Image, saves it, show it"""
		
		# create image
		self.image = Image.new(
			mode  = "RGB", 
			size  = (int(self.image_size/2)*len(self.strange_word), self.image_size + 50), 
			color = self.txt_color
		)
		
		draw = ImageDraw.Draw(self.image)

		# draw text
		draw.text(
			(10,10),
			self.strange_word,
			font=self.font,
			fill=(255,255,0)
		)
		
	
	def save_image(self):
		# save file
		self.image.save(self.file_name)