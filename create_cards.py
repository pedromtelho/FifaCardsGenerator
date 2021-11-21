import requests
import bs4
import json
from PIL import Image,ImageDraw,ImageFont
import time
import os
import shutil

# , 'silver.txt', 'brass.txt'
list_types = ['gold.txt']

for item in list_types:
    with open(item, encoding='utf8') as f:
        for line in f:
            if line != "\n":
                try:
                    result = requests.get('https://www.fifarosters.com/lookupfutplayer.php?term='+line+'&no_blank=true&year=21')

                    result = result.json()
                    result = result[0]

                    # Nome carta final
                    card = "card_"+result["label"]+"_"+result["data"]["firstname"]+".png"

                    # Rosto
                    response = requests.get(result["img_url"])
                    rosto = "rosto_"+result["label"]+"_"+result["data"]["firstname"]+".png"
                    file = open(rosto, "wb")
                    file.write(response.content)
                    file.close()

                    # Bandeira
                    nation = result["nation"]
                    soup = bs4.BeautifulSoup(nation, "html.parser")
                    response = requests.get(soup.img['src'])
                    bandeira = "bandeira_"+result["label"]+"_"+result["data"]["firstname"]+".png"
                    file = open(bandeira, "wb")
                    file.write(response.content)
                    file.close()

                    # Time
                    time_link = soup.img['src'].split("/")
                    time_link = time_link[0] + "//" + time_link[2] + "/" + time_link[3] + "/clubs/" + "fifa21/" + result['data']['clubid'] + ".png"
                    response = requests.get(time_link)
                    time_jogador = "time_"+result["label"]+"_"+result["data"]["firstname"]+".png"
                    file = open(time_jogador, "wb")
                    file.write(response.content)
                    file.close()

                    # Ajusta o tamanho das imagens
                    def resize_image(first_image, new_width, new_height):
                        img = Image.open(first_image) 
                        new_width  = new_width
                        new_height = new_height
                        img = img.resize((new_width, new_height), Image.ANTIALIAS)
                        img.save(first_image)

                    resize_image(rosto, 342, 402)
                    resize_image(bandeira, 75, 45)
                    resize_image(time_jogador, 69, 69)

                    # Sobrepõe imagens
                    def overlay_images(first, second, third, fourth, x1, y1, x2, y2, x3, y3, output_img_name):
                        first_image = Image.open(first).convert('RGBA')

                        second_image = Image.open(second).convert('RGBA')
                        third_image = Image.open(third).convert('RGBA')
                        fourth_image = Image.open(fourth).convert('RGBA')

                        
                        first_image.paste(second_image, (x1,y1), second_image)
                        first_image.paste(third_image, (x2,y2), third_image)
                        first_image.paste(fourth_image, (x3,y3), fourth_image)
                        

                        first_image.save(output_img_name)
                    overlay_images("dourado_design.png", rosto, bandeira, time_jogador, 188, 50, 130, 255, 134, 330, card)

                    # Escreve informações dos jogadores

                    def center_text(img, font, text, x, y, name=None, img_name=None):
                        if name != None:
                            draw = ImageDraw.Draw(img)
                            text_width, text_height = draw.textsize(text, font)
                            position = ((590-text_width)/2,455)
                            draw.text(position, text, fill='#46390c', font=font)
                            return img.save(img_name)
                        else:
                            draw = ImageDraw.Draw(img)
                            position = (x,y)
                            draw.text(position, text, fill='#46390c', font=font)
                            return img.save(img_name)

                    rating = result["data"]["rating"]
                    pos = result["data"]["position"]
                    sho = result["data"]["sho"]
                    pas = result["data"]["longpassing"]
                    pac = result["data"]["pac"]
                    dri = result["data"]["dribbling"]
                    phy = result["data"]["phy"]
                    defi = result["data"]["def"]

                    # Nome
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 45), result["label"], 0, 0, name="name", img_name=card)

                    # Rating + position
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 100), rating, 115, 100, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 25), pos, 147, 200, img_name=card)

                    # Numbers
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 47), pac, 120, 517, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 47), sho, 120, 571, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 47), pas, 120, 625, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 45), dri, 335, 517, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 45), defi, 335, 571, img_name=card)
                    center_text(Image.open(card).convert('RGBA'), ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 45), phy, 335, 625, img_name=card)
                    os.remove(rosto)
                    os.remove(bandeira)
                    os.remove(time_jogador)
                    shutil.move(card, "./cards")
                    time.sleep(10)
                except:
                    print("Jogador "+ line + " não tem link")