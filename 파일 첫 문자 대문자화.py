import textwrap
import os
from tkinter import ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.request import urlopen


filestonomen = filedialog.askopenfilenames(title="이미지를 선택하시오", filetypes=(("모든파일", "*.*"),("PNG파일", "*.png")),
                                            initialdir=r"C:\OneDrive\Drug structure DB")
list = []
list2 = []
for file in filestonomen:
    # nomenmoleculae.append(file[int(file.rfind("/"))+1 : int(len(file))-4])
    list2.append(file[int(file.rfind("/")) + 1: int(len(file)) - 4])
    namae = file[int(file.rfind("/")) + 1: int(len(file)) - 4]
    namae2 = file[int(file.rfind("/")) + 1].upper() + file[int(file.rfind("/")) + 2: int(len(file)) - 4]
    list.append(namae2)
print(list)


dir = r'C:\OneDrive\Drug structure DB\'

for ind, i in enumerate(list):
    old_file = dir+f"\{list2[ind]}.png"
    new_file = dir+f"\{i}.png"
    os.rename(old_file, new_file)

