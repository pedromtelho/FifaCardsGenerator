from PIL import Image,ImageDraw,ImageFont

# # sample text and font
# unicode_text = u"Hello World!"
# font = ImageFont.truetype(, 50, encoding="unic")

# # get the line size
# text_width, text_height = font.getsize(unicode_text)

# # create a blank canvas with extra space between lines
# canvas = 
# # draw the text onto the text canvas, and use black as the text color
# draw = ImageDraw.Draw(canvas)
# draw.text((295,455), u'MESSI', , font=font, anchor='ms')

# # save the blank canvas to a file
# # canvas.save("unicode-text.png", "PNG")
# canvas.show()

def center_text(img, font, text):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((590-text_width)/2,455)
    draw.text(position, text, fill='#46390c', font=font)
    return img.show()
center_text(Image.open("card_MESSI_Lionel.png").convert('RGBA'), "/usr/share/fonts/truetype/freefont/FreeSans.ttf", "MESSI")