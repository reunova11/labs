import os
import csv
mypath=os.getcwd()
from PIL import Image, ImageFilter
import os.path
#os.mkdir("pictures_new")
a=len([f for f in os.listdir(mypath)
    if f.endswith('.jpg') and os.path.isfile(os.path.join(mypath, f))])
b=[f for f in os.listdir(mypath)
    if f.endswith('.jpg') and os.path.isfile(os.path.join(mypath, f))]
for i in range(a):
    im=str(b[i])
    with Image.open(im) as img:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save('pictures_new/'+im+".jpg")
        #img.show()
def n1():
    # os.mkdir("pictures_new")
    myPath = os.getcwd()
    r = input("Изображения какого расширения вы хотите обработать?: ")
    if r == '.jpg':
        a = len([f for f in os.listdir(myPath)
                    if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))])
        b = [f for f in os.listdir(myPath)
                if f.endswith('.jpg') and os.path.isfile(os.path.join(myPath, f))]
        for i in range(a):
            im = str(b[i])
            with Image.open(im) as img:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                # img.save('pictures_new/' + im + r)
                img.show()
    if r == '.png':
        a = len([f for f in os.listdir(myPath)
                    if f.endswith('.png') and os.path.isfile(os.path.join(myPath, f))])
        b = [f for f in os.listdir(myPath)
            if f.endswith('.png') and os.path.isfile(os.path.join(myPath, f))]
        for i in range(a):
            im = str(b[i])
            with Image.open(im) as img:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                img.save('pictures_new/' + im + r)
                img.show()
#n1()
def n2():
    with open("data.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        sum=0
        st=1
        print("Нужно купить: ")
        for row in file_reader:
            print(f'    {row[0]} - {row[1]} шт. за  {row[2]} руб.')
            st=int(row[1]) * int(row[2])
            sum+=st
    print("Итоговая сумма: ", sum, " руб." )
n2()