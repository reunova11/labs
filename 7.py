from PIL import Image
filename = "пр.jpg"
with Image.open(filename) as img:
    img.load()
img.show()
size = img.size
format = img.format
mode = img.mode
print("Размер: ", size)
print("Формат: ", format)
print("Цветовая модель: ", mode)

def n1():
    from PIL import Image
    filename = "3.jpg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_3.jpg")
n1()
def n2():
    from PIL import Image
    for i in range(1,6):
        im = str(i) + '.jpg'
        with Image.open(im) as img:
            gray_img = img.convert("L")
            gray_img = gray_img.show()
            gray_img.save('pictures/'+str(im))
n2()
def n3():
    s = int(input("Сколько изображений вы хотите обработать? "))
    for i in range(0,s):
        u = str(i) +'.jpg'
        image_path = input("Введите название файла с учетом .jpg ")
        watermark_path = input("Введите название водяного знака с учетом .png ")
        im = Image.open(image_path)
        watermark = Image.open(watermark_path)
        watermark1 = watermark.reduce(3)
        im.paste(watermark1, (1,1))
        im.show()
        im.save(str(u))
n3()