import cv2 
import easygui 
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import *
import messagebox


def upload():
    global path1,path,I
    ImagePath=easygui.fileopenbox()

    newName="cartoonified_Image"
    path1=os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    I = "Image saved by name " + newName +" at "+ path
    cartoonify(ImagePath)

def cartoonify(ImagePath): 
        global ReSized6
        originalmage = cv2.imread(ImagePath)
        originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)

        if originalmage is None:
            print("Can not find any image. Choose appropriate file")
            sys.exit()
        ReSized1 = cv2.resize(originalmage, (960, 540))
        grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
        ReSized2 = cv2.resize(grayScaleImage, (960, 540))
        smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
        ReSized3 = cv2.resize(smoothGrayScale, (960, 540))
        getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        ReSized4 = cv2.resize(getEdge, (960, 540))
        colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300)
        ReSized5 = cv2.resize(colorImage, (960, 540))
        cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
        ReSized6 = cv2.resize(cartoonImage, (960, 540))
        images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
        fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
        for i, ax in enumerate(axes.flat):
            ax.imshow(images[i], cmap='gray')
        save1=Button(top,text="Save cartoon image",command=lambda: save(),padx=30,pady=5)
        save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
        save1.pack(side=TOP,pady=50)   
        plt.show()
def save(): 
    messagebox.showinfo(title=None, message=I)
top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))
upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)
top.mainloop()
cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))

        
        



        
        
