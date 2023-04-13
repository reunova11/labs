from PIL import Image
o = Image.open('8m.jpg')
o.show()
o = o.crop((50, 150, 300, 500))
o.show()
o.save("8_new.jpg")
def n1():
    from PIL import Image
    spisok = {"Новый год": "ng.jpg", "День матери": "md.jpg", "День рождения": "dr.jpg", "8 марта":"8m.jpg"}
    l = input("Выберите праздник ")
    praz = spisok.get(l)
    Image = Image.open(praz)
    Image.show()
n1()
def n2():
    from PIL import Image, ImageDraw, ImageFont
    o = Image.open('8m.jpg')
    im = input("Введите имя поздравляемого ")
    txt = str(im) + ", поздравляю!"
    img_txt = ImageDraw.Draw(o)
    font = ImageFont.truetype("impact.ttf", size=65)
    img_txt.text((50, 600), txt, font=font, fill="red")
    o.show()
    o.save("neew.png")
n2()