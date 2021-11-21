from PIL import Image

def resize_image(first_image, new_width, new_height):
    img = Image.open(first_image) # image extension *.png,*.jpg
    new_width  = new_width
    new_height = new_height
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(first_image) 

resize_image("braziliantricks.jpg", 400, 400)