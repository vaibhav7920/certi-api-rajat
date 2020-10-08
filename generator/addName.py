from PIL import ImageFont, ImageDraw, Image
fontColour = (70, 121, 189)
fontSize = 40

font = ImageFont.truetype('generator/fonts/roman.ttf', fontSize)


def gen_certificate(name):
	xCoordinate = 780
	yCoordinate = 425
	template = 'templates/template.jpg'
	img = Image.open(template)
	draw = ImageDraw.Draw(img)
	draw.text((xCoordinate, yCoordinate), name, font=font, fill=fontColour)
	img = img.convert('RGB')
	img.save(f"certificate.pdf")
