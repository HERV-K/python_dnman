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

# 무언가 버튼을 누르면 라벨의 내용을 지우고 무슨 작업이 실행되었는지 알려주어야
#db에 추가하는 기능 추가해야

#neowindow1 : 약이름명 받고 리스트 만들기

root = Tk()

root.title("drug db management system")
root.geometry("1000x500+100+50")





def calculateimagesize(imagetocal):
    #imagetocal은 크기 계산할 이미지,, 반환값은 리스트 [w, h]
    image = Image.open(imagetocal)
    width = image.size[0]
    height = image.size[1]
    return [width, height]

def changeimagesize(imagetochange, multiple):
    #첫 녀석은 이미지,, 2번놈은 배수이다.
    image = Image.open(imagetochange)
    imagesize = calculateimagesize(imagetochange)
    image9 = image.resize((int(imagesize[0])*int(multiple)),(int(imagesize[1])*int(multiple)))
    return image9

def changeimagesize2(imagetochange, size):
    #이 녀석은 사진의 더 긴 변의 길이를 입력값(size)로 비율 유지하며 줄이는 녀석
    image = Image.open(imagetochange)
    imagesize = calculateimagesize(imagetochange)
    if imagesize[0] >= imagesize[1]:
        image9 = image.resize((int(size), round(int(imagesize[1]) * int(size)/int(imagesize[0]))))
    else:
        image9 = image.resize((round(int(imagesize[0]) * int(size)/int(imagesize[1])), int(size)))
    return image9
    pass


def openneowindow1():
    global neowindow1
    neowindow1 = Toplevel(root)
    neowindow1.geometry("1200x600+300+150")

    w1_label_top = Label(neowindow1, text="생성할 파일의 이름을 아래에 입력하세영")
    w1_label_top.grid(row=1,column=1,columnspan=5,sticky=N+W+E+S)

    w1_ent_newfilename = Entry(neowindow1)
    w1_ent_newfilename.grid(row=2,column=1,columnspan=4,sticky=N+W+E+S)

    def maketemptxtfile():
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w1temporalfile = open(PATHtosave, "a", encoding="utf8")
        w1temporalfile.close()
        w1_label_top.config(text="txt파일이 생성되었읍니다.")


    w1_btn_getnewfilename = Button(neowindow1,text="입력완료", width=10, command= maketemptxtfile)
    w1_btn_getnewfilename.grid(row=2,column=5,sticky=N+W+E+S)

    w1_ent_drugname1 = Entry(neowindow1, width=25)
    w1_ent_drugname1.grid(row=2,column=6,sticky=N+W+E+S)
    w1_ent_drugname2 = Entry(neowindow1, width=25)
    w1_ent_drugname2.grid(row=3, column=6, sticky=N + W + E + S)
    w1_ent_drugname3 = Entry(neowindow1, width=25)
    w1_ent_drugname3.grid(row=4, column=6, sticky=N + W + E + S)
    w1_ent_drugname4 = Entry(neowindow1, width=25)
    w1_ent_drugname4.grid(row=5, column=6, sticky=N + W + E + S)
    w1_ent_drugname5 = Entry(neowindow1, width=25)
    w1_ent_drugname5.grid(row=6, column=6, sticky=N + W + E + S)
    w1_ent_drugname6 = Entry(neowindow1, width=25)
    w1_ent_drugname6.grid(row=7, column=6, sticky=N + W + E + S)
    w1_ent_drugname7 = Entry(neowindow1, width=25)
    w1_ent_drugname7.grid(row=8, column=6, sticky=N + W + E + S)
    w1_ent_drugname8 = Entry(neowindow1, width=25)
    w1_ent_drugname8.grid(row=9, column=6, sticky=N + W + E + S)
    w1_ent_drugname9 = Entry(neowindow1, width=25)
    w1_ent_drugname9.grid(row=  10, column=6, sticky=N + W + E + S)
    w1_ent_drugname10 = Entry(neowindow1, width=25)
    w1_ent_drugname10.grid(row=11, column=6, sticky=N + W + E + S)

    w1_ent_drugname11 = Entry(neowindow1, width=25)
    w1_ent_drugname11.grid(row=2, column=7, sticky=N + W + E + S)
    w1_ent_drugname12 = Entry(neowindow1, width=25)
    w1_ent_drugname12.grid(row=3, column=7, sticky=N + W + E + S)
    w1_ent_drugname13 = Entry(neowindow1, width=25)
    w1_ent_drugname13.grid(row=4, column=7, sticky=N + W + E + S)
    w1_ent_drugname14 = Entry(neowindow1, width=25)
    w1_ent_drugname14.grid(row=5, column=7, sticky=N + W + E + S)
    w1_ent_drugname15 = Entry(neowindow1, width=25)
    w1_ent_drugname15.grid(row=6, column=7, sticky=N + W + E + S)
    w1_ent_drugname16 = Entry(neowindow1, width=25)
    w1_ent_drugname16.grid(row=7, column=7, sticky=N + W + E + S)
    w1_ent_drugname17 = Entry(neowindow1, width=25)
    w1_ent_drugname17.grid(row=8, column=7, sticky=N + W + E + S)
    w1_ent_drugname18 = Entry(neowindow1, width=25)
    w1_ent_drugname18.grid(row=9, column=7, sticky=N + W + E + S)
    w1_ent_drugname19 = Entry(neowindow1, width=25)
    w1_ent_drugname19.grid(row=10, column=7, sticky=N + W + E + S)
    w1_ent_drugname20 = Entry(neowindow1, width=25)
    w1_ent_drugname20.grid(row=11, column=7, sticky=N + W + E + S)

    w1_ent_drugname21 = Entry(neowindow1, width=25)
    w1_ent_drugname21.grid(row=2, column=8, sticky=N + W + E + S)
    w1_ent_drugname22 = Entry(neowindow1, width=25)
    w1_ent_drugname22.grid(row=3, column=8, sticky=N + W + E + S)
    w1_ent_drugname23 = Entry(neowindow1, width=25)
    w1_ent_drugname23.grid(row=4, column=8, sticky=N + W + E + S)
    w1_ent_drugname24 = Entry(neowindow1, width=25)
    w1_ent_drugname24.grid(row=5, column=8, sticky=N + W + E + S)
    w1_ent_drugname25 = Entry(neowindow1, width=25)
    w1_ent_drugname25.grid(row=6, column=8, sticky=N + W + E + S)
    w1_ent_drugname26 = Entry(neowindow1, width=25)
    w1_ent_drugname26.grid(row=7, column=8, sticky=N + W + E + S)
    w1_ent_drugname27 = Entry(neowindow1, width=25)
    w1_ent_drugname27.grid(row=8, column=8, sticky=N + W + E + S)
    w1_ent_drugname28 = Entry(neowindow1, width=25)
    w1_ent_drugname28.grid(row=9, column=8, sticky=N + W + E + S)
    w1_ent_drugname29 = Entry(neowindow1, width=25)
    w1_ent_drugname29.grid(row=10, column=8, sticky=N + W + E + S)
    w1_ent_drugname30 = Entry(neowindow1, width=25)
    w1_ent_drugname30.grid(row=11, column=8, sticky=N + W + E + S)

    w1_ent_drugname31 = Entry(neowindow1, width=25)
    w1_ent_drugname31.grid(row=2, column=9, sticky=N + W + E + S)
    w1_ent_drugname32 = Entry(neowindow1, width=25)
    w1_ent_drugname32.grid(row=3, column=9, sticky=N + W + E + S)
    w1_ent_drugname33 = Entry(neowindow1, width=25)
    w1_ent_drugname33.grid(row=4, column=9, sticky=N + W + E + S)
    w1_ent_drugname34 = Entry(neowindow1, width=25)
    w1_ent_drugname34.grid(row=5, column=9, sticky=N + W + E + S)
    w1_ent_drugname35 = Entry(neowindow1, width=25)
    w1_ent_drugname35.grid(row=6, column=9, sticky=N + W + E + S)
    w1_ent_drugname36 = Entry(neowindow1, width=25)
    w1_ent_drugname36.grid(row=7, column=9, sticky=N + W + E + S)
    w1_ent_drugname37 = Entry(neowindow1, width=25)
    w1_ent_drugname37.grid(row=8, column=9, sticky=N + W + E + S)
    w1_ent_drugname38 = Entry(neowindow1, width=25)
    w1_ent_drugname38.grid(row=9, column=9, sticky=N + W + E + S)
    w1_ent_drugname39 = Entry(neowindow1, width=25)
    w1_ent_drugname39.grid(row=10, column=9, sticky=N + W + E + S)
    w1_ent_drugname40 = Entry(neowindow1, width=25)
    w1_ent_drugname40.grid(row=11, column=9, sticky=N + W + E + S)

    def getentname():
        list1 = []
        list1.append(w1_ent_drugname1.get())
        list1.append(w1_ent_drugname2.get())
        list1.append(w1_ent_drugname3.get())
        list1.append(w1_ent_drugname4.get())
        list1.append(w1_ent_drugname5.get())
        list1.append(w1_ent_drugname6.get())
        list1.append(w1_ent_drugname7.get())
        list1.append(w1_ent_drugname8.get())
        list1.append(w1_ent_drugname9.get())
        list1.append(w1_ent_drugname10.get())
        list1.append(w1_ent_drugname11.get())
        list1.append(w1_ent_drugname12.get())
        list1.append(w1_ent_drugname13.get())
        list1.append(w1_ent_drugname14.get())
        list1.append(w1_ent_drugname15.get())
        list1.append(w1_ent_drugname16.get())
        list1.append(w1_ent_drugname17.get())
        list1.append(w1_ent_drugname18.get())
        list1.append(w1_ent_drugname19.get())
        list1.append(w1_ent_drugname20.get())
        list1.append(w1_ent_drugname21.get())
        list1.append(w1_ent_drugname22.get())
        list1.append(w1_ent_drugname23.get())
        list1.append(w1_ent_drugname24.get())
        list1.append(w1_ent_drugname25.get())
        list1.append(w1_ent_drugname26.get())
        list1.append(w1_ent_drugname27.get())
        list1.append(w1_ent_drugname28.get())
        list1.append(w1_ent_drugname29.get())
        list1.append(w1_ent_drugname30.get())
        list1.append(w1_ent_drugname31.get())
        list1.append(w1_ent_drugname32.get())
        list1.append(w1_ent_drugname33.get())
        list1.append(w1_ent_drugname34.get())
        list1.append(w1_ent_drugname35.get())
        list1.append(w1_ent_drugname36.get())
        list1.append(w1_ent_drugname37.get())
        list1.append(w1_ent_drugname38.get())
        list1.append(w1_ent_drugname39.get())
        list1.append(w1_ent_drugname40.get())
        return list1
        pass


    def w1drugnameentered():
        print(getentname())
        listofenteredname = getentname()
        list2 = []
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w1txtfiletoaddnames = open(PATHtosave, "a", encoding="utf8")
        for ind, i in enumerate(listofenteredname):
            if i != "":
                drugname = str(i[0].upper())+str(i[1:len(i)])
                list2.append(drugname)
                w1txtfiletoaddnames.write(f"{str(drugname)} : \n")
            else:
                pass
        print(list2)
        w1txtfiletoaddnames.close()
        label_direction.config(text="약물명 입력이 완료되었읍니다.")
        label_direction.update()

        """
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w1temporalfile = open(PATHtosave, "a", encoding="utf8")
        w1temporalfile.close()
        w1_label_top.config(text="txt파일이 생성되었읍니다.")
        """


        pass

    w1_btn_drugnameentry = Button(neowindow1, text="입력완료", width=10, command=w1drugnameentered)
    w1_btn_drugnameentry.grid(row=11, column=9, sticky=N + W + E + S)

    def w1drugnamesort():
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w1txtfiletosort = open(PATHtosave, "r", encoding="utf8")
        lines = w1txtfiletosort.readlines()
        w1dic1 = {}
        for ind, i in enumerate(lines):
            w1dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w1txtfiletosort.close()
        sorteddic = dict(sorted(w1dic1.items()))
        w1txtfiletosort = open(PATHtosave, "w", encoding="utf8")
        for code, name in sorteddic.items():
            w1txtfiletosort.write(f"{code} : {name}\n")
        w1txtfiletosort.close()
        label_direction.config(text="정렬이 완료되었읍니다.")
        label_direction.update()
        pass

    w1_btn_drugnamesort = Button(neowindow1, text="정렬", width=10, command=w1drugnamesort)
    w1_btn_drugnamesort.grid(row=12, column=9, sticky=N + W + E + S)


    ##############################################################################''
    def w2getsmile():
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w2txttoopen = open(PATHtosave, "r", encoding="utf8")
        lines = w2txttoopen.readlines()
        w2dic1 = {}
        for ind, i in enumerate(lines):
            w2dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w2done1 = list(w2dic1.keys())
        w2txttoopen.close()
        ###여기까지 txt파일의 약물명을 받아오는 부분

        browser = webdriver.Chrome()
        # browser.maximize_window()
        url = "https://go.drugbank.com/"
        listtofind = w2done1
        smilelist = []
        iupaclist = []

        for i in listtofind:
            browser.get(url)
            searchtab = browser.find_element(By.CLASS_NAME, "search-query")
            searchtab.send_keys(i)
            button = browser.find_element(By.CLASS_NAME, "input-group-append")
            button.click()
            parent = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[2]/dl[6]")
            dt = parent.find_elements(By.TAG_NAME, "dt")
            dd = parent.find_elements(By.TAG_NAME, "dd")
            listdttxt = []
            for ind in dt:
                listdttxt.append(ind.text)
            listddtxt = []
            for ind in dd:
                listddtxt.append(ind.text)
            dtd = list(zip(listdttxt, listddtxt))
            smilelist.append(dtd[len(dtd) - 1][1])
            iupaclist.append(dtd[len(dtd) - 2][1])
            print(i)
            print(dtd[len(dtd) - 1][1])
            print(dtd[len(dtd) - 2][1])
            nameandsmile = list(zip(listtofind, smilelist))
            nameandiupac = list(zip(listtofind, iupaclist))
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}.txt"
        w2txttowritesmiledb = open(PATHtosave, "r", encoding="utf8")
        lines = w2txttowritesmiledb.readlines()
        w2dic_old = {}
        w2dic_new = {}

        for ind, i in enumerate(lines):
            w2dic_old[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
        w2txttowritesmiledb.close()

        for ind, i in enumerate(listtofind):
            if i in w2dic_old:
                w2dic_old[i] = smilelist[ind]
            else:
                w2dic_new[i] = smilelist[ind]

        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w2txttowritesmiledb = open(PATHtosave, "w", encoding="utf8")

        for code, name in w2dic_old.items():
            w2txttowritesmiledb.write(f"{code} : {name}\n")
        for code, name in w2dic_new.items():
            w2txttowritesmiledb.write(f"{code} : {name}\n")
        w2txttowritesmiledb.close()
        w1_label_top.config(text="smiles 생성이 완료되었읍니다.")
        w1_label_top.update()
        browser.close()


        pass

    def w2getstructure():
        browser = webdriver.Chrome()
        # browser.maximize_window()
        url = "http://cdb.ics.uci.edu/cgibin/Smi2DepictWeb.py"

        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w2txttofindstr = open(PATHtosave, "r", encoding="utf8")
        lines = w2txttofindstr.readlines()
        w2dic1 = {}
        for ind, i in enumerate(lines):
            w2dic1[i[0:i.index(":")-1]] = i[i.index(":")+2 : i.index("\n")]
        w2done1 = list(w2dic1.keys())
        w2txttofindstr.close()

        browser.get(url)
        searchtab = browser.find_element(By.ID, "smiles")
        searchtab.clear()


        for ind, i in enumerate(w2dic1):
            searchtab.send_keys(w2dic1[i])
            searchtab.send_keys(Keys.RETURN)

        btn = browser.find_element(By.XPATH, '//*[@id="Smi2DepictWeb"]/div[1]/div[5]/button')
        btn.click()

        time.sleep(2)
        img3 = browser.find_elements(By.CLASS_NAME, "shadow")

        foldername = str(w1_ent_newfilename.get())


        PATH = "C:\OneDrive\Drug structure DB"
        #PATHtosave = PATH + f"\{filename}_result.txt"
        PATHtocheck = PATH + f"\{foldername}"
        if os.path.exists(PATHtocheck) == True:
            pass
        else:
            os.mkdir(path = PATHtocheck)
            pass

        for index, image in enumerate(img3):
            src = image.get_attribute("src")
            t = urlopen(src).read()
            file = open(os.path.join(PATHtocheck, f"{w2done1[index]}.png"), "wb")
            file.write(t)
            print(w2done1[index])
        browser.close()

    def w2gogo():
        w2getsmile()
        w2getstructure()
        w1_label_top.config(text="구조 생성이 완료되었읍니다.")
        w1_label_top.update()
        pass
    #############################################################################


    w1_btn_makestr = Button(neowindow1, text="구조 생성", width=10, command=w2gogo)
    w1_btn_makestr.grid(row=13, column=9, sticky=N + W + E + S)



driveurl_pythofolder = r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt"


def showdbonmainscreen():
    label_direction.config(text="")
    text_screen_big.delete("1.0", END)
    file_drugnamedb = open(driveurl_pythofolder,"r",encoding="utf8")
    lines = file_drugnamedb.readlines()
    dic_dblist = {}
    for ind, i in enumerate(lines):
        dic_dblist[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
        #text_screen_big.insert(END, f'{"{0:0=4}".format(ind+1)}. {i[0:i.index(":") - 1]} {i[i.index(":") + 2:len(i) - 1]}\n')
        text_screen_big.insert(END,f'{"{0:0=4}".format(ind + 1)}. {"{" ":40}".format(i[0:i.index(":") - 1])} {i[i.index(":") + 2:len(i) - 1]}\n')
    file_drugnamedb.close()
    print("db를 스크린에 띄웁니당..")
    label_direction.config(text="DB를 스크린에 띄웠읍니다.")
    pass

btn_showdb = Button(root, text="db보기", width=10, command=showdbonmainscreen)
btn_showdb.grid(row=0, column=1,sticky=N+W+E+S)

def sortdb():
    label_direction.config(text="")
    file_drugnamedb = open(driveurl_pythofolder, "r", encoding="utf8")
    lines = file_drugnamedb.readlines()
    print(lines)
    dic1 = {}
    for ind, i in enumerate(lines):
        print(str(i[0].upper()) + str(i[1:i.index(":") - 1]))
        dic1[str(i[0].upper()) + str(i[1:i.index(":") - 1])] = i[i.index(":") + 2: i.index("\n")]
    file_drugnamedb.close()
    done1 = dict(sorted(dic1.items()))
    print(list(done1.keys()))
    file_drugnamedb = open(driveurl_pythofolder, "w", encoding="utf8")
    for code, name in done1.items():
        file_drugnamedb.write(f"{code} : {name}\n")
    file_drugnamedb.close()
    pass

btn_sortdb = Button(root, text="db정렬", width=10, command=sortdb)
btn_sortdb.grid(row=0, column=2,sticky=N+W+E+S)

btn_openneowindow1 = Button(root, text="약물구조", width=20,command=openneowindow1)
btn_openneowindow1.grid(row=1, column=7,sticky=N+W+E+S)

btn_openneowindow2 = Button(root, text="DB에 한글명 넣기", width=20, command=openneowindow3)
btn_openneowindow2.grid(row=2, column=7,sticky=N+W+E+S)

##스크린#########################################################################
scrollbar_mainscreen = Scrollbar(root)
scrollbar_mainscreen.grid(row=1,column=6,rowspan=10, sticky=N+W+E+S)
text_screen_big = Text(root, yscrollcommand=scrollbar_mainscreen.set)
text_screen_big.grid(row=1,column=1,columnspan=5,rowspan=10, sticky=N+W+E+S)
scrollbar_mainscreen.config(command=text_screen_big.yview)
################################################################################

label_direction = Label(root, text="라벨이무니다")
label_direction.grid(row=11, column=1, columnspan=5, sticky=N+W+E+S)



root.mainloop()
while (True):
    pass