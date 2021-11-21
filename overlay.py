from PIL import Image

def overlay_images(first, second, third, fourth, x1, y1, x2, y2, x3, y3, output_img_name):
    first_image = Image.open(first).convert('RGBA')

    second_image = Image.open(second).convert('RGBA')
    third_image = Image.open(third).convert('RGBA')
    fourth_image = Image.open(fourth).convert('RGBA')

    
    first_image.paste(second_image, (x1,y1), second_image)
    first_image.paste(third_image, (x2,y2), third_image)
    first_image.paste(fourth_image, (x3,y3), fourth_image)
    

    first_image.save(output_img_name)
overlay_images("dourado_design.png", "rosto_MESSI_Lionel.png", "bandeira_MESSI_Lionel.png", "time_MESSI_Lionel.png", 190, 70, 130, 255, 134, 330, "card_MESSI_Lionel.png")
