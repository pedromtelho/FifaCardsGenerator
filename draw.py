from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("card.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("SourceCodePro-Bold.ttf", 30)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.show()