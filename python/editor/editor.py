from PyQt5.QtWidgets import (
   QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget,QHBoxLayout, QVBoxLayout
)
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)
import os
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")

but_folder = QPushButton("Папка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Вправо")
but_mirrow= QPushButton("Дзеркально")
but_blur = QPushButton("Різкість")
but_bw = QPushButton("Ч/Б")

list = QListWidget()
label_img = QLabel("Картинка")

lineH = QHBoxLayout()
lineH2 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineV1.addWidget(but_folder)
lineV1.addWidget(list)
lineH2.addWidget(but_left)
lineH2.addWidget(but_right)
lineH2.addWidget(but_mirrow)
lineH2.addWidget(but_blur)
lineH2.addWidget(but_bw)
lineV2.addWidget(label_img)
lineV2.addLayout(lineH2)

lineH.addLayout(lineV1)
lineH.addLayout(lineV2)

win.setLayout(lineH)

win.show()
def filter(files,imgshow):
    result=[]
    for filename in files:
        for e in imgshow:
            if filename.endswith(e):
                result.append(filename)
    return result
workdir = ""    
def showDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def showfile():
    imgshow=[".jpg",".jpeg", ".gif", ".png", ".bmp"]
    showDir()
    filenames = filter(os.listdir(workdir),imgshow)
    list.clear()
    for filename in filenames:
        list.addItem(filename)

but_folder.clicked.connect(showfile)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modefile/"
    
    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        label_img.hide()
        piximg = QPixmap(path)
        w, h = label_img.width(), label_img.height()
        piximg = piximg.scaled(w,h,Qt.KeepAspectRatio)
        label_img.setPixmap(piximg)
        label_img.show()
    def saveImage(self):
       ''' зберігає копію файлу у підпапці '''
       path = os.path.join(self.dir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       image_path = os.path.join(path, self.filename)
       self.image.save(image_path)
    

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path)


    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir,self.save_dir,self.filename)
        self.showImage(image_path)

def choseImage():
    if list.currentRow()>=0:
        filename = list.currentItem().text()
        workimg.loadImage(workdir,filename)
        image_path = os.path.join(workimg.dir, workimg.filename)
        workimg.showImage(image_path)

workimg = ImageProcessor()
list.currentRowChanged.connect(choseImage)
but_bw.clicked.connect(workimg.do_bw)
but_left.clicked.connect(workimg.do_left)
but_right.clicked.connect(workimg.do_right)
but_mirrow.clicked.connect(workimg.do_mirror)
but_blur.clicked.connect(workimg.do_blur)
app.exec_()