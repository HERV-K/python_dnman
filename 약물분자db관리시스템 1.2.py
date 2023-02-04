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
import pyautogui as pygui
import cv2

# 무언가 버튼을 누르면 라벨의 내용을 지우고 무슨 작업이 실행되었는지 알려주어야
#db에 추가하는 기능 추가해야


# 윈도우1에서 입력이 완료된 파일을 약 10~20개씩 묶어 인터넷 검색하다가 오류 났을 때 처음부터 다시해야 하는 것을 방지하는 기능 추가해야


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

        ### smile 저장과 구조 저장을 분리하자..

        browser = webdriver.Chrome()
        browser.maximize_window()
        url = "https://go.drugbank.com/"
        listtofind = w2done1
        smilelist = []
        iupaclist = []
        text_screen_big.delete("1.0", END)
        for i in listtofind:
            browser.get(url)
            searchtab = browser.find_element(By.CLASS_NAME, "search-query")
            searchtab.send_keys(i)
            button = browser.find_element(By.CLASS_NAME, "input-group-append")
            button.click()

            parent = browser.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[1]")
            print(len(parent.find_elements(By.TAG_NAME, "h1")))

            tester1 = len(parent.find_elements(By.TAG_NAME, "h1"))
            if tester1 ==0:
                print("ERROR")
                text_screen_big.insert(END, f"{i}\n")
                smilelist.append(" ")
                w1_btn_getsmileagain.config(bg = "red", fg="white")
                w1_btn_getsmileagain.update()
            else:
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



            # parent = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[2]/dl[6]")
            # dt = parent.find_elements(By.TAG_NAME, "dt")
            # dd = parent.find_elements(By.TAG_NAME, "dd")
            # listdttxt = []
            # for ind in dt:
            #     listdttxt.append(ind.text)
            # listddtxt = []
            # for ind in dd:
            #     listddtxt.append(ind.text)
            # dtd = list(zip(listdttxt, listddtxt))
            # smilelist.append(dtd[len(dtd) - 1][1])
            # iupaclist.append(dtd[len(dtd) - 2][1])
            # print(i)
            # print(dtd[len(dtd) - 1][1])
            # print(dtd[len(dtd) - 2][1])
            # nameandsmile = list(zip(listtofind, smilelist))
            # nameandiupac = list(zip(listtofind, iupaclist))
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


    def w2getsmileagain():
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w2txttofindstr = open(PATHtosave, "r", encoding="utf8")
        lines = w2txttofindstr.readlines()
        w2dic1 = {}
        for ind, i in enumerate(lines):
            w2dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w2done1 = list(w2dic1.keys())
        w2txttofindstr.close()

        for ind, i in enumerate(w2done1):
            if w2dic1[i] == " ":
                #인터넷 통해 검색하는 코드
                browser = webdriver.Chrome()
                browser.maximize_window()
                url = "https://go.drugbank.com/"
                browser.get(url)
                searchtab = browser.find_element(By.CLASS_NAME, "search-query")
                searchtab.send_keys(i)
                button = browser.find_element(By.CLASS_NAME, "input-group-append")
                button.click()

                parent = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[1]")
                print(len(parent.find_elements(By.TAG_NAME, "h1")))

                tester1 = len(parent.find_elements(By.TAG_NAME, "h1"))
                if tester1 == 0:
                    print("ERROR")
                    text_screen_big.insert(END, f"{i}\n")
                    w2dic1[i] = " "
                    w1_btn_getsmileagain.config(bg="red", fg="white")
                    w1_btn_getsmileagain.update()
                else:
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
                    w2dic1[i] = dtd[len(dtd) - 1][1]

            else:
                # 그냥 넘어감
                pass

        #
        filename = w1_ent_newfilename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w2txttowritesmiledb = open(PATHtosave, "w", encoding="utf8")

        for code, name in w2dic1.items():
            w2txttowritesmiledb.write(f"{code} : {name}\n")
        w2txttowritesmiledb.close()
        w1_label_top.config(text="smiles 생성이 완료되었읍니다.")
        w1_label_top.update()
        browser.close()


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


    w1_btn_makestr = Button(neowindow1, text="예비", width=10, command=w2gogo)
    w1_btn_makestr.grid(row=13, column=9, sticky=N + W + E + S)

    w1_btn_getsmile = Button(neowindow1, text="SMILE얻기", width=10, command=w2getsmile)
    w1_btn_getsmile.grid(row=14, column=9, sticky=N + W + E + S)

    w1_btn_getsmileagain = Button(neowindow1, text="result의SMILE조정", width=10, command=w2getsmileagain)
    w1_btn_getsmileagain.grid(row=15, column=9, sticky=N + W + E + S)

    w1_btn_getstr = Button(neowindow1, text="구조얻기", width=10, command=w2getstructure)
    w1_btn_getstr.grid(row=16, column=9, sticky=N + W + E + S)

def openneowindow3():
    global neowindow3
    neowindow3 = Toplevel(root)
    neowindow3.geometry("1200x600+100+100")
    global nomenkoreae
    nomenkoreae = []
    def choosefilestonomenclate():
        global filestonomen
        filestonomen = filedialog.askopenfilenames(title="이미지를 선택하시오", filetypes=(("모든파일", "*.*"),("PNG파일", "*.png")),
                                            initialdir=r"C:\OneDrive\Drug structure DB")
        #아래는 각 분자사진 파일의 분자이름을 리스트에 담는다.
        global nomenmoleculae
        nomenmoleculae = []
        text_w3_screen.delete("1.0",END)
        for file in filestonomen:
            # nomenmoleculae.append(file[int(file.rfind("/"))+1 : int(len(file))-4])
            namae = file[int(file.rfind("/"))+1 : int(len(file))-4]
            namae2 = file[int(file.rfind("/"))+1].upper() + file[int(file.rfind("/"))+2 : int(len(file))-4]
            nomenmoleculae.append(namae2)
            print(calculateimagesize(file))
            """
            #버튼에 분자구조 보여주는 방법
            photo = changeimagesize2(file,150)
            photo2 = ImageTk.PhotoImage(photo)
            btn_w3_molecularstr.config(image = photo2)
            btn_w3_molecularstr.update()
            time.sleep(0.1)
            """
        print("nomenmoleculae는 ",nomenmoleculae," 입니다.")
        #아래는 불러온 분자의 이름 리스트를 스크린에 표시되게 한다.
        for ind, i in enumerate(nomenmoleculae):
            text_w3_screen.insert(END, f"{i} : {calculateimagesize(filestonomen[ind])[0]}x{calculateimagesize(filestonomen[ind])[1]}\n")

        drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "r", encoding="utf8")
        lines = drugnamedb_read.readlines()
        dic_dblist = {}
        for ind, i in enumerate(lines):
            dic_dblist[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
        drugnamedb_read.close()
        label_w3_molecularname.config(text=dic_dblist[nomenmoleculae[0]])
        label_w3_molecularname.update()
        if nomenmoleculae[0] in dic_dblist:
            nomenkoreae.append(str(dic_dblist[nomenmoleculae[0]]))
            ent_w3_koreanname.delete(0, END)
            ent_w3_koreanname.insert(0, dic_dblist[nomenmoleculae[0]])
        else:
            ent_w3_koreanname.delete(0, END)

        btn_w3_molecularstr.mainloop()

    global filestonomen
    global nomenmoleculae
    def w3_start():

        def w3compnowmolecule(listname, index):
            listname = nomenkoreae
            # listname은 한국명 리스트
            drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "r", encoding="utf8")
            lines = drugnamedb_read.readlines()
            dic_dblist = {}
            for ind, i in enumerate(lines):
                dic_dblist[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
            drugnamedb_read.close()

            if len(ent_w3_koreanname.get()) == 0:
                if nomenmoleculae[index - 1] in dic_dblist:
                    listname.append(str(dic_dblist[nomenmoleculae[index-1]]))
                    ent_w3_koreanname.delete(0,END)
                else:
                    listname.append(ent_w3_koreanname.get())
                    ent_w3_koreanname.delete(0,END)
            else:
                listname.append(ent_w3_koreanname.get())
                ent_w3_koreanname.delete(0,END)

        def w3compnextmolecule(index):
            drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "r", encoding="utf8")
            lines = drugnamedb_read.readlines()
            dic_dblist = {}
            for ind, i in enumerate(lines):
                dic_dblist[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
            drugnamedb_read.close()

            if nomenmoleculae[index] in dic_dblist:
                ent_w3_koreanname.delete(0,END)
                ent_w3_koreanname.insert(0,dic_dblist[nomenmoleculae[index]])
                ent_w3_koreanname.update()
            else:
                ent_w3_koreanname.delete(0,END)

        global w3opvalue
        w3opvalue = 1
        def w3operate():
            global w3opvalue

            if w3opvalue == 1:
                if len(nomenmoleculae) == 1:
                    label_w3_molecularname.config(text="끝")
                    if len(nomenkoreae) ==1:
                        pass
                    else:
                        nomenkoreae.append(str(ent_w3_koreanname.get()))
                    ###텍스트 이미지 만드는 코드 넣어야
                    ent_w3_koreanname.delete(0,END)
                    msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")
                    w3opvalue +=1


                else:
                    label_w3_molecularname.config(text=nomenmoleculae[w3opvalue])
                    photo = changeimagesize2(filestonomen[w3opvalue],200)
                    photo2 = ImageTk.PhotoImage(photo)
                    btn_w3_molecularstr.config(image = photo2)
                    btn_w3_molecularstr.update
                    label_w3_molecularname.update()

                    if len(nomenkoreae) ==0:
                        nomenkoreae.append(str(ent_w3_koreanname.get()))
                        ent_w3_koreanname.delete(0,END)
                    else:
                        pass
                    w3compnextmolecule(w3opvalue)
                    print(nomenkoreae)
                    w3opvalue +=1


            elif 1 < w3opvalue <= len(nomenmoleculae)-1:
                label_w3_molecularname.config(text=nomenmoleculae[w3opvalue])
                photo = changeimagesize2(filestonomen[w3opvalue], 200)
                photo2 = ImageTk.PhotoImage(photo)
                btn_w3_molecularstr.config(image=photo2)
                btn_w3_molecularstr.update
                label_w3_molecularname.update()
                w3compnowmolecule(nomenkoreae,w3opvalue)
                w3compnextmolecule(w3opvalue)
                print(nomenkoreae)
                w3opvalue+=1


            elif w3opvalue == len(nomenmoleculae):
                label_w3_molecularname.config(text="입력이 완료되었읍니다. 버튼은 사진제작")
                btn_w3_getkoreanname.config(bg="red", text="")
                ##테이블 만드는 버튼도 켜야 한다.
                w3compnowmolecule(nomenkoreae, w3opvalue)
                print(nomenkoreae)
                w3opvalue+=1


            else:
                pass
                #사진 이미지 만들고 등등의 작업은 여기서 이루어진다.
                # maketextimages(listofkoreanname)
                # btn_maketable.config(bg="blue")
                # btn_savetodb.config(bg="green")
                # msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")
                # label_molecularname.config(text="db를 저장하세영", bg="red")
                msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")
                # w3opvalue = 1
            # btn_w3_molecularstr.update()
            btn_w3_molecularstr.mainloop()


        btn_w3_getkoreanname = Button(neowindow3, text="한국명 입력완료", bg="white", width=40, height=1, command=w3operate)
        btn_w3_getkoreanname.grid(row=7, column=3, columnspan=2, sticky=W + E + N + S)
        btn_w3_getkoreanname.config(bg="green")
        btn_w3_getkoreanname.update()

        photo = changeimagesize2(filestonomen[0], 200)
        photo2 = ImageTk.PhotoImage(photo)
        btn_w3_molecularstr.config(image=photo2)
        btn_w3_molecularstr.update()

        btn_w3_getkoreanname.config(bg="white")
        btn_w3_molecularstr.mainloop()
        pass

    def w3_savetodb():
        global nomenmoleculae
        global nomenkoreae

        nomenmoleculae2 = nomenmoleculae[0:len(nomenkoreae)]

        drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "r", encoding="utf8")
        lines = drugnamedb_read.readlines()
        dic_oldver = {}
        dic_tobaeadded = {}
        for ind, i in enumerate(lines):
            dic_oldver[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
        drugnamedb_read.close()

        for ind, i in enumerate(nomenmoleculae2):
            if i in dic_oldver:
                dic_oldver[i] = nomenkoreae[ind]
                print(nomenkoreae[ind])
            else:
                dic_tobaeadded[i] = nomenkoreae[ind]
                print(nomenkoreae[ind])
        drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "w", encoding="utf8")
        for code, name in dic_oldver.items():
            drugnamedb_read.write(f'{code} : {name}\n')
        for code, name in dic_tobaeadded.items():
            drugnamedb_read.write(f'{code} : {name}\n')
        drugnamedb_read.close()
        msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")



    def w3_makeindphoto():

        pass

    btn_w3_choosefile = Button(neowindow3, text="파일 선택",width=20, command=choosefilestonomenclate)
    btn_w3_choosefile.grid(row=1,column=1,sticky=W+E+N+S)
    btn_w3_1 = Button(neowindow3, text="예비1",width=20)
    btn_w3_1.grid(row=1, column=2, sticky=W + E + N + S)
    btn_w3_2 = Button(neowindow3, text="예비2", width=20)
    btn_w3_2.grid(row=1, column=3, sticky=W + E + N + S)
    btn_w3_3 = Button(neowindow3, text="명명 시작", width=20, command=w3_start)
    btn_w3_3.grid(row=1, column=4, sticky=W + E + N + S)

    text_w3_screen = Text(neowindow3, height=25)
    text_w3_screen.grid(row=2, column=1,columnspan=4, rowspan=4 ,sticky=W+E+N+S)

    label_w3_molecularname = Label(neowindow3, text="분자의 이름")
    label_w3_molecularname.grid(row=6, column=1,columnspan=2,sticky=W+E+N+S)

    ent_w3_koreanname = Entry(neowindow3)
    ent_w3_koreanname.grid(row=6, column=3,columnspan=2,sticky=W+E+N+S)

    # btn_w3_getkoreanname = Button(neowindow3, text="한국명 입력완료", bg="white", width=40, height=1)
    # btn_w3_getkoreanname.grid(row=7, column=3,columnspan=2,sticky=W+E+N+S)

    btn_w3_4 = Button(neowindow3, text="db에 저장", width=40, height=1, command=w3_savetodb)
    btn_w3_4.grid(row=8, column=3,columnspan=2, sticky=W + E + N + S)

    btn_w3_5 = Button(neowindow3, text="사진만들기", width=40, height=1, command=w3_makeindphoto)
    btn_w3_5.grid(row=9, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_6 = Button(neowindow3, text="예비6", width=40, height=1)
    btn_w3_6.grid(row=10, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_7 = Button(neowindow3, text="예비7", width=40, height=1)
    btn_w3_7.grid(row=11, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_8 = Button(neowindow3, text="예비8", width=40, height=1)
    btn_w3_8.grid(row=12, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_9 = Button(neowindow3, text="예비9", width=40, height=1)
    btn_w3_9.grid(row=13, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_10 = Button(neowindow3, text="예비10", width=40, height=1)
    btn_w3_10.grid(row=14, column=3, columnspan=2, sticky=W + E + N + S)

    btn_w3_molecularstr = Button(neowindow3,text="분자구조",width=40 ,height=8)
    btn_w3_molecularstr.grid(row=7, column=1, columnspan=2, rowspan=8, sticky=W + E + N + S)


def openneowindow4():
    global neowindow4
    neowindow4 = Toplevel(root)
    neowindow4.geometry("1200x700+100+100")
    global w4_count
    w4_count=0


    def w4_choosefile():
        #파일을 받아오는 창을 연다
        global filetomakeimgs
        filetomakeimgs = filedialog.askopenfilenames(title="이미지를 선택하시오", filetypes=(("모든파일", "*.*"), ("PNG파일", "*.png")),
                                                   initialdir=r"C:\OneDrive\Drug structure DB")

    def browse_path():
        global w4_folder_selected
        w4_folder_selected = filedialog.askdirectory()
        btn_w4_makeindimg.config(fg="black")
        btn_w4_makeindimg.update()
        btn_w4_maketable.config(fg="black")
        btn_w4_maketable.update()


    def w4_check():
        global filetomakeimgs
        global w4_nomenlistofimgs
        global w4_nomenkoreae
        #받아온 파일들의 분자명을 리스트화한다.
        w4_nomenlistofimgs = []
        for file in filetomakeimgs:
            w4_nomenlistofimgs.append(file[int(file.rfind("/")) + 1: int(len(file)) - 4])
        print(w4_nomenlistofimgs)

        #db를 열어 읽어들인 것을 딕셔너리에 저장하고 닫는다.
        drugnamedb_read = open(r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt", "r", encoding="utf8")
        lines = drugnamedb_read.readlines()
        w4_dic_dblist = {}
        for ind, i in enumerate(lines):
            w4_dic_dblist[i[0:i.index(":") - 1]] = i[i.index(":") + 2:len(i) - 1]
        drugnamedb_read.close()

        # 분자명 리스트에 대응하는 한국명 리스트를 만든다.
        w4_nomenkoreae = []
        for ind, i in enumerate(w4_nomenlistofimgs):
            if w4_dic_dblist.get(i,"none") != "none":
                w4_nomenkoreae.append(w4_dic_dblist[i])
                text_w4_screen.insert(END,f'{"{" ":40}".format(i)} : {w4_dic_dblist[i]}\n')
                text_w4_screen.update()
                #text_w4_screen.insert(END, f"{"{" ":40}".format(i)} : {w4_dic_dblist[i]}\n")
            else:
                text_w4_screen.insert(END,f'{"{" ":40}".format(i)} : ERROR\n')
                #text_w4_screen.insert(END, f"{"{" ":40}".format(i)} : ERROR\n")
                text_w4_screen.update()
                btn_w4_checkdb.config(bg="red")
                btn_w4_checkdb.update()
                msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")



        if len(w4_nomenlistofimgs) == len(w4_nomenkoreae):
            #zip한 결과를 딕셔너리화
            global w4_dic_moleculename
            w4_dic_moleculename = {}
            for ind, i in enumerate(w4_nomenlistofimgs):
                w4_dic_moleculename[i] = w4_nomenkoreae[ind]
        else:
            pass
        btn_w4_makeindimg.config(bg="green", fg="green")
        btn_w4_makeindimg.update()
        btn_w4_maketable.config(bg="green", fg="green")
        btn_w4_maketable.update()
        btn_w4_2.config(text=len(w4_nomenlistofimgs))


    margintesterwideng = []
    margintesterheieng = []
    margintesterwidkor = []
    margintesterheikor = []


    def w4_saveindimg(img,text1):
        global w4_folder_selected
        pathway = os.path.join(w4_folder_selected, f"{text1}.png")
        img.save(pathway)
        pass

    def w4_makeindimgs_1(text1, text2, image):
        #이 녀석은 바로 실행된다기 보단ㄴ,,, 다른 함수에 넣어서 사용해야 할 듯
        #text는 사진에 넣을 문장을 뜻함
        #1. 글자 이미지 생성

        ##1-1. 텍스트 이미지 사이즈
        widthoftextimg = int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")])
        heightoftextimg = int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*3/8)

        ##1-2. 텍스트 포함 여부

        ##1-3. 글자의 색상
        if combox_w4_fontcol.get() == "빨":
            font_color = "RGBA(255, 051, 051, 255)"
        elif combox_w4_fontcol.get() == "검":
            font_color = "RGBA(000, 051, 255, 255)" ## 편집 필요
        elif combox_w4_fontcol.get() == "노":
            font_color = "RGBA(255, 204,000, 255)"
        elif combox_w4_fontcol.get() == "초":
            font_color = "RGBA(000, 153, 000, 255)"
        else:
            font_color = "RGBA(000, 051, 255, 255)"

        ##1-4. 글꼴
        if combox_w4_font.get() == "쿠키런":
            fontstyle = r"C:\OneDrive\Drug structure DB\dbmansys\fonts\CookieRun Regular.ttf"
        elif combox_w4_font.get() == "천년":
            fontstyle = r"C:\OneDrive\Drug structure DB\dbmansys\fonts\경기천년바탕_Regular.ttf"
        elif combox_w4_font.get() == "우리금융":
            fontstyle = r"C:\OneDrive\Drug structure DB\dbmansys\fonts\우리다움 R.ttf"
        else:
            fontstyle = r"C:\OneDrive\Drug structure DB\dbmansys\fonts\HANBatang.ttf"

        ##1-5. 기타 상수
        global backgroundcolor
        # backgroundcolor = "RGBA(0,0,0,0)"  # 글자 배경색
        fontsizetempeng = int(heightoftextimg/3)
        fontsizetempkor = int(heightoftextimg / 3)

        ##1-6. 폰트, 문장의 크기
        len_engletter = len(text1)
        len_korletter = len(text2)

        if len_engletter <= 10:
            #fontsizetempeng = int(heightoftextimg/2 -15)
            fontsizetempeng = int(heightoftextimg / 3 - 7)
        elif 10< len_engletter <=15:
            fontsizetempeng = int(heightoftextimg / 3 - 7)
        elif 15 < len_engletter <= 20:
            fontsizetempeng = int(heightoftextimg / 4 - 10)
        else:
            fontsizetempeng = int(heightoftextimg / 4 - 10)

        if len_korletter <=5:
            #fontsizetempkor = int(heightoftextimg/3 + 3)
            fontsizetempkor = int(heightoftextimg / 4)
        elif 5<len_korletter <= 9:
            fontsizetempkor = int(heightoftextimg / 4)
        else:
            fontsizetempkor = int(heightoftextimg / 5)


        fonttempeng = ImageFont.truetype(font=fontstyle, size=fontsizetempeng)
        fonttempkor = ImageFont.truetype(font=fontstyle, size=fontsizetempkor)# 여기서 조정한 폰트사이즈가 설정되기에,, 지우면 안됨
        wid_engbox = fonttempeng.getbbox(text1)[2]
        hei_engbox = fonttempeng.getbbox(text1)[3]
        wid_korbox = fonttempkor.getbbox(text2)[2]
        hei_korbox = fonttempkor.getbbox(text2)[3]


        totalwidmargineng = widthoftextimg -  wid_engbox
        totalwidmarginkor = widthoftextimg - wid_korbox
        totalheimargin = heightoftextimg - hei_korbox - hei_engbox
        # margintesterwideng.append(totalwidmargineng)
        # margintesterwidkor.append(totalwidmarginkor)
        # margintesterheieng.append(totalheimargin)
        # print(f"margin : 한  {totalwidmarginkor}  &영  {totalwidmargineng}  x  {totalheimargin}   | 영문 : {text1}, len={len_engletter}, box : {wid_engbox}x{hei_engbox} | 한글 : {text2}, len={len_korletter}, box : {wid_korbox}x{hei_korbox}")

        ##1-7.텍스트이미지 제작
        if combox_w4_contkor.get() =="아니오":

            x_eng = int((widthoftextimg - wid_engbox) / 2)
            y_eng = int(totalheimargin / 2)
            x_kor = int((widthoftextimg - wid_korbox) / 2)
            y_kor = y_eng + int(hei_engbox)

            textedimg = Image.new("RGBA", (widthoftextimg, heightoftextimg), color=backgroundcolor)
            draw = ImageDraw.Draw(textedimg)
            draw.text((x_eng, y_eng), " ", font=fonttempeng, fill=font_color)
            draw.text((x_kor, y_kor), " ", font=fonttempkor, fill=font_color)
            ##
            #
            pass
        else:
            x_eng = int((widthoftextimg - wid_engbox)/2)
            y_eng = int(totalheimargin/2)
            x_kor = int((widthoftextimg - wid_korbox)/2)
            y_kor = y_eng + int(hei_engbox)

            textedimg = Image.new("RGBA", (widthoftextimg, heightoftextimg), color = backgroundcolor)
            draw = ImageDraw.Draw(textedimg)
            draw.text((x_eng,y_eng),text1, font=fonttempeng, fill=font_color)
            draw.text((x_kor,y_kor), text2, font=fonttempkor, fill=font_color)

        #2. 사진들 덧대기
        ##2-1. 사진 크기 결정
        photo = Image.open(image)
        tempwid_img = photo.size[0]
        temphei_img = photo.size[1]




        if float(tempwid_img/temphei_img) >= float(400/250):
            #wid를 줄인다.
            img9 = photo.resize((int(widthoftextimg), int(temphei_img*widthoftextimg/tempwid_img)))
            #print(int(widthoftextimg), int(temphei_img*widthoftextimg/tempwid_img))
        else:
            img9 = photo.resize((int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img), int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)))
            #print((int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img), int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)))
            #hei를 줄인다.

        adjustedimg = img9
        ##2-2. 사진, 텍스트 덧대기
        resultimg = Image.new("RGBA", (int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]), int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])), color=backgroundcolor)
        # print((int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]), int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])))
        if float(tempwid_img/temphei_img) >= float(400/250):
            resultimg.paste(adjustedimg, (0, int(((int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)) - int(temphei_img*widthoftextimg/tempwid_img))/2)))
            resultimg.paste(textedimg, (0, int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:]) * 5 / 8)))
            # resultimg.show()
            return resultimg
        else:
            #  int((int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]) -  int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img))/2)
            resultimg.paste(adjustedimg, (int((int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]) -  int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img))/2), 0))
            resultimg.paste(textedimg, (0, int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:]) * 5 / 8)))
            # resultimg.show()
            return resultimg

        ##2-3. 저장
        # global w4_folder_selected
        # pathway = os.path.join(w4_folder_selected, f"{text1}.png")
        # resultimg.save(pathway)

        #각 콤박스별로 만들 이미지 속성 받아오는 코드 필요


    def w4_makeindimgs():
        global w4_dic_moleculename  # 한국어, 영어 이름 딕셔너리임
        global filetomakeimgs
        global w4_nomenlistofimgs
        global w4_nomenkoreae
        global w4_count

        global backgroundcolor
        backgroundcolor = "RGBA(0,0,0,0)"

        for ind, file in enumerate(filetomakeimgs):
            w4_saveindimg(w4_makeindimgs_1(str(w4_nomenlistofimgs[ind]),str(w4_nomenkoreae[ind]), file), str(w4_nomenlistofimgs[ind]))
            w4_count+=1
            btn_w4_2.config(text=len(w4_nomenlistofimgs)-w4_count)
            btn_w4_2.update()
        # margintesterwideng.sort()
        # margintesterwidkor.sort()
        # margintesterheieng.sort()
        # print(f"wid eng{margintesterwideng}\nwid kor{margintesterwidkor}\nhei{margintesterheieng}")
        msgbox.showinfo("무야히", "무야하")
        w4_count = 0
        pass

    def w4_maketable():
        global w4_dic_moleculename  # 한국어, 영어 이름 딕셔너리임
        global filetomakeimgs
        global w4_nomenlistofimgs
        global w4_nomenkoreae
        global w4_count

        global backgroundcolor
        backgroundcolor = "RGBA(255,255,255,255)"

        listofmadeimg = []
        for ind, file in enumerate(filetomakeimgs):
            listofmadeimg.append(w4_makeindimgs_1(str(w4_nomenlistofimgs[ind]),str(w4_nomenkoreae[ind]), file))
            w4_count += 1
            btn_w4_2.config(text=len(w4_nomenlistofimgs) - w4_count)
            btn_w4_2.update()

        columnnum =int(combox_w4_layout.get()[0:combox_w4_layout.get().rfind("x")])
        rownum =int(combox_w4_layout.get()[combox_w4_layout.get().rfind("x") + 1:])
        print(columnnum, rownum)

        pagenum = 1 + int(len(listofmadeimg)/(columnnum*rownum))
        print(pagenum)
        pagelist = []
        for a in range(1, pagenum +1):
            pagelist.append(f"page{a}")
            pagelist[a-1] = Image.new("RGBA", (int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]) * columnnum, int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:])*rownum), (255,255,255,255))
            print(f"페이지번호 : {a}")
            for b in range(1, rownum+1):
                print(f"{a}번 페이지의 {b}번줄")
                for c in range(1, columnnum+1):
                    if columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b <= len(listofmadeimg)-1:
                        print(f"{a}번 페이지의 {b}번줄의 {c}번 칼럼에는 {columnnum * rownum * (a - 1) + (columnnum + 1) * (b - 1) + c - b}가 들어간다.")

                        # listofmadeimg[int(columnnum * rownum * (a - 1) + (columnnum + 1) * (b - 1) + c - b)].show()

                        pagelist[a-1].paste(listofmadeimg[int(columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b)], (int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")])*(c-1)-c+1, int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:])*(b-1)-b+1))

                        # widthoftextimg = int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")])
                        # heightoftextimg = int(
                        #     int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:]) * 3 / 8)

                        # listlist[a-1].paste(photo8, ( (c-1)*525-c+1 +int((525 - width_img) / 2), (b-1)*594-b+1 +int((524 - height_img) / 2) ))
                        pass
                    else:
                        break
                if columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b <= len(listofmadeimg)-1:
                    pass
                else:
                    break
            if columnnum * rownum * (a - 1) + (columnnum + 1) * (b - 1) + c - b <= len(listofmadeimg) - 1:
                pass
            else:
                break

        for ind, i in enumerate(pagelist):
            pathway_jpg = os.path.join(r"C:\OneDrive\Drug structure DB\Tables",
                                       f"table of {ent_w4_filename.get()}__{ind}.png")
            i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
            i.save(pathway_jpg)
            print("저장완료")


        # global w4_folder_selected

        # for ind, i in enumerate(pagelist):
        #     pathway_png = os.path.join(r"C:\OneDrive\Drug structure DB\Tables", f"table of {ent_w4_filename.get()}_{ind}.png")
        #     pathway_jpg = os.path.join(r"C:\OneDrive\Drug structure DB\Tables", f"table of {ent_w4_filename.get()}__{ind}.png")
        #     # i.show()
        #     # i.save(pathway_png)
        #     # i = i.resize((int(i.size[0]/2),int(i.size[1]/2)))
        #     phase1 = 0
        #     for a in range(0, i.size[0]):
        #         phase1 = int((100*(a+1)/i.size[0]))
        #         btn_w4_2.config(text = phase1)
        #         btn_w4_2.update()
        #         for b in range(0, i.size[1]):
        #             rgba = i.getpixel((a, b))
        #             if rgba[3] == 0:
        #                 i.putpixel((a,b), (255, 255, 255, 255))
        #             else:
        #                 pass
        #     i.save(pathway_jpg)
        print("END")





        #     w4_makeindimgs_1(str(w4_nomenlistofimgs[ind]), str(w4_nomenkoreae[ind]), file), str(w4_nomenlistofimgs[ind])
        #
        #
        #     w4_count += 1
        #     btn_w4_2.config(text=len(w4_nomenlistofimgs) - w4_count)
        #     btn_w4_2.update()
        # # margintesterwideng.sort()
        # # margintesterwidkor.sort()
        # # margintesterheieng.sort()
        # # print(f"wid eng{margintesterwideng}\nwid kor{margintesterwidkor}\nhei{margintesterheieng}")
        # msgbox.showinfo("무야히", "무야하")
        # w4_count = 0
        pass




    label_w4_alarm = Label(neowindow4,text="파일의 이름을 정하세영")
    label_w4_alarm.grid(row=0,column=1, sticky=W + E + N + S)

    ent_w4_filename = Entry(neowindow4)
    ent_w4_filename.grid(row=0,column=2,columnspan=3, sticky=W + E + N + S)

    btn_w4_choosefile = Button(neowindow4,width=20, text="파일선택", command=w4_choosefile)
    btn_w4_choosefile.grid(row=1,column=1, sticky=W + E + N + S)

    btn_w4_checkdb = Button(neowindow4, width=20, text="검사", command = w4_check)
    btn_w4_checkdb.grid(row=1, column=2, sticky=W + E + N + S)

    btn_w4_1 = Button(neowindow4, width=20, text="저장경로 선택", command=browse_path)
    btn_w4_1.grid(row=1, column=3, sticky=W + E + N + S)

    btn_w4_2 = Button(neowindow4, width=20, text="예비2")
    btn_w4_2.grid(row=1, column=4, sticky=W + E + N + S)

    text_w4_screen = Text(neowindow4, height=25)
    text_w4_screen.grid(row=2, column=1, columnspan=4, rowspan=10, sticky=W + E + N + S)

    btn_w4_makeindimg = Button(neowindow4,text="개별사진", width=20, bg="white",fg="white", command=w4_makeindimgs)
    btn_w4_makeindimg.grid(row=5, column=5, sticky=W + E + N + S)

    listofindimgsize = ["800x800","400x400", "자율"]
    combox_w4_indimgsize = ttk.Combobox(neowindow4,values = listofindimgsize)#, state="readonly")
    combox_w4_indimgsize.current(0)
    combox_w4_indimgsize.grid(row=4, column=5, sticky=W + E + N + S)

    Yesorno = ["약품명 포함?", "예", "아니오"]
    combox_w4_contkor = ttk.Combobox(neowindow4, values=Yesorno, state="readonly")
    combox_w4_contkor.current(0)
    combox_w4_contkor.grid(row=3, column=5, sticky=W + E + N + S)

    fontcolourlist = ["폰트색(검정)", "빨", "노", "초", "파"]
    combox_w4_fontcol = ttk.Combobox(neowindow4, values=fontcolourlist, state="readonly")
    combox_w4_fontcol.current(0)
    combox_w4_fontcol.grid(row=2, column=5, sticky=W + E + N + S)

    fontlist = ["폰트(기본)", "쿠키런", "천년", "우리금융"]
    combox_w4_font = ttk.Combobox(neowindow4, values=fontlist, state="readonly")
    combox_w4_font.current(0)
    combox_w4_font.grid(row=2, column=6, sticky=W + E + N + S)



    btn_w4_maketable = Button(neowindow4, text="장표", bg="white", fg="white", width=20, command=w4_maketable)
    btn_w4_maketable.grid(row=11, column=5, sticky=W + E + N + S)

    layoutlist = ["5x6","4x5","4x4", "5x5","6x6", "5x7"]

    combox_w4_layout = ttk.Combobox(neowindow4, values = layoutlist, state = "readonly")
    combox_w4_layout.current(0)
    combox_w4_layout.grid(row=10, column=5, sticky=W + E + N + S)

def openneowindow5():
    global neowindow5
    neowindow5 = Toplevel(root)
    neowindow5.geometry("1200x700+100+100")


    def openchemsketch():
        # 2. 켐스케치 버튼을 누른다.
        icon_chemsketch = pygui.locateOnScreen("chemsketchicon.png", confidence=0.7, region=(
        168, 1027, 1452 - 168, 1078 - 1027))  # region = (x, y, wid, hei) )
        print(icon_chemsketch)
        pygui.click(icon_chemsketch)
        print("켐스케치를 실행합니다.")
        pygui.sleep(3)

        # 3. 화면창에서 ok버튼을 누른다.
        icon_chemsketchokbutton = pygui.locateOnScreen("chemsketch_okbutton.png", confidence=0.96)
        while icon_chemsketchokbutton is None:
            icon_chemsketchokbutton = pygui.locateOnScreen("chemsketch_okbutton.png", confidence=0.96)
            print("시ㄹ패")
        pygui.click(icon_chemsketchokbutton)
        print("빈 화면이 나타납ㅂ니다.")
        pygui.sleep(2)
        global openedwindow
        # 4. 전체화면을 만든다.
        openedwindow = pygui.getActiveWindow()
        openedwindow.maximize()
        print(openedwindow.title)



        # #################
        ################
        ############# preference에서 비율 고정을 선택한다.
        pass

    def opensmileenterwin():
        global openedwindow
        #5. smile 입력창을 연다.
        openedwindow.activate()
        pygui.sleep(3)
        icon_toolsbutton = pygui.locateOnScreen("chemsketch_toolsbutton.png", confidence=0.99)
        pygui.click(icon_toolsbutton, duration = 0.1)
        print("tools를 눌렀읍니다.")
        pygui.sleep(0.1)

        icon_generatebutton = pygui.locateOnScreen("chemsketch_generatebutton.png", confidence=0.99)
        pygui.click(icon_generatebutton, duration = 0.1)
        print("generate를 눌렀읍니다.")
        pygui.sleep(0.1)

        icon_formsmilebutton = pygui.locateOnScreen("chemsketch_fromsmilebutton.png", confidence=0.99)
        pygui.click(icon_formsmilebutton, duration = 0.1)
        print("smile로 만들기 창으로 진입합니다.")
        pygui.sleep(0.5)
        """
        # 6-1. 파일에서 목록을 불러온다.

        filename = ent_w5_filename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w5txttofindstr = open(PATHtosave, "r", encoding="utf8")
        lines = w5txttofindstr.readlines()
        w5dic1 = {}
        for ind, i in enumerate(lines):
            w5dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w5done1 = list(w5dic1.keys())
        w5txttofindstr.close()

        
        # 6-2. 입력창에 smile을 입력합니다.
        smilewindow = pygui.getActiveWindow()
        smilewindow.activate()
        pygui.sleep(0.1)
        pygui.write("aaaas@@[s]s", interval=0.07)
        """

    def makestructures():
        global openedwindow
        #6-1 파일목록 불ㄹ오기
        filename = ent_w5_filename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w5txttofindstr = open(PATHtosave, "r", encoding="utf8")
        lines = w5txttofindstr.readlines()
        w5dic1 = {}
        for ind, i in enumerate(lines):
            w5dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w5done1 = list(w5dic1.keys())
        w5txttofindstr.close()

        #6-2 파일목록의 약물 입력
        openedwindow.activate()
        pygui.sleep(3)

        for ind, i in enumerate(w5done1):
            icon_toolsbutton = pygui.locateOnScreen("chemsketch_toolsbutton.png", confidence=0.99)
            pygui.click(icon_toolsbutton, duration=0.05)
            print("tools를 눌렀읍니다.")
            pygui.sleep(0.1)

            icon_generatebutton = pygui.locateOnScreen("chemsketch_generatebutton.png", confidence=0.99)
            pygui.click(icon_generatebutton, duration=0.05)
            print("generate를 눌렀읍니다.")
            pygui.sleep(0.1)

            icon_formsmilebutton = pygui.locateOnScreen("chemsketch_fromsmilebutton.png", confidence=0.99)
            pygui.click(icon_formsmilebutton, duration=0.05)
            print("smile로 만들기 창으로 진입합니다.")
            pygui.sleep(0.5)
            smilewindow = pygui.getActiveWindow()
            smilewindow.activate()
            pygui.sleep(0.1)
            pygui.write(w5dic1[i], interval=0.003)
            pygui.keyDown("enter")
            pygui.sleep(0.2)
            pygui.keyDown("enter")
            pygui.sleep(0.2)
            #966,422 30,31,34 #1E1F22
            pygui.click(966, 850)
            pygui.sleep(0.3)


            icon_nextpagebutton = pygui.locateOnScreen("chemsketch_nextpagebutton.png", confidence=0.99)
            pygui.click(icon_nextpagebutton, duration=0.1)
            pygui.sleep(0.3)

    def saveimages():
        global openedwindow
        pygui.sleep(5)
        filename = ent_w5_filename.get()
        PATH = "C:\OneDrive\Drug structure DB\dbmansys"
        PATHtosave = PATH + f"\{filename}_result.txt"
        w5txttofindstr = open(PATHtosave, "r", encoding="utf8")
        lines = w5txttofindstr.readlines()
        w5dic1 = {}
        for ind, i in enumerate(lines):
            w5dic1[i[0:i.index(":") - 1]] = i[i.index(":") + 2: i.index("\n")]
        w5done1 = list(w5dic1.keys())
        w5txttofindstr.close()


        pygui.sleep(1)


        for ind, i in enumerate(w5done1):
            icon_filesbutton = pygui.locateOnScreen("chemsketch_filesbutton.png", confidence=0.99)
            pygui.click(icon_filesbutton, duration=0.1)
            print("tools를 눌렀읍니다.")
            pygui.sleep(0.1)

            icon_saveasbutton = pygui.locateOnScreen("chemsketch_saveasbutton.png", confidence=0.99)
            pygui.click(icon_saveasbutton, duration=0.1)
            pygui.sleep(1)

            #####
            smilewindow = pygui.getActiveWindow()
            smilewindow.activate()
            pygui.sleep(0.1)
            pygui.write(i, interval=0.03)
            pygui.keyDown("tab")
            pygui.sleep(0.1)
            ####

            icon_savefileformatbutton = pygui.locateOnScreen("chemsketch_savefileformatbutton.png", confidence=0.99)
            pygui.click(icon_savefileformatbutton, duration=0.1)
            pygui.sleep(0.15)

            icon_pngbutton = pygui.locateOnScreen("chemsketch_pngbutton.png")
            pygui.click(icon_pngbutton, duration=0.1)
            pygui.sleep(0.2)

            pygui.keyDown("enter")
            pygui.sleep(0.5)
            icon_saveyesbutton = pygui.locateOnScreen("chemsketch_saveyesbutton.png")
            pygui.click(icon_saveyesbutton, duration=0.1)
            pygui.sleep(0.5)

            icon_savenextpagebutton = pygui.locateOnScreen("chemsketch_savenextpagebutton.png")
            pygui.click(icon_savenextpagebutton, duration=0.1)
            pygui.sleep(0.3)






        pass





    label_w5_alarm = Label(neowindow5, text="파일의 이름을 정하세영")
    label_w5_alarm.grid(row=0, column=1, sticky=W + E + N + S)

    ent_w5_filename = Entry(neowindow5)
    ent_w5_filename.grid(row=0, column=2, columnspan=3, sticky=W + E + N + S)

    btn_w5_choosefile = Button(neowindow5, width=20, text="파일선택")
    btn_w5_choosefile.grid(row=1, column=1, sticky=W + E + N + S)

    btn_w5_checkdb = Button(neowindow5, width=20, text="검사")
    btn_w5_checkdb.grid(row=1, column=2, sticky=W + E + N + S)

    btn_w5_1 = Button(neowindow5, width=20, text="저장경로 선택")
    btn_w5_1.grid(row=1, column=3, sticky=W + E + N + S)

    btn_w5_2 = Button(neowindow5, width=20, text="예비2")
    btn_w5_2.grid(row=1, column=4, sticky=W + E + N + S)

    btn_w5_3 = Button(neowindow5, text = "켐스케치 실행" , width=20, command=openchemsketch)
    btn_w5_3.grid(row=2, column=1, sticky=W + E + N + S)

    btn_w5_4 = Button(neowindow5, width=20, text="테스트.." , command=opensmileenterwin)
    btn_w5_4.grid(row=2, column=2, sticky=W + E + N + S)

    btn_w5_5 = Button(neowindow5, width=20, text="구조만들기", command=makestructures)
    btn_w5_5.grid(row=2, column=3, sticky=W + E + N + S)

    btn_w5_6 = Button(neowindow5, width=20, text="저장(첫사진저장해야)", command=saveimages)
    btn_w5_6.grid(row=2, column=4, sticky=W + E + N + S)

    text_w5_screen = Text(neowindow5, height=25)
    text_w5_screen.grid(row=3, column=1, columnspan=4, rowspan=10, sticky=W + E + N + S)

    btn_w5_makeindimg = Button(neowindow5, text="개별사진", width=20, bg="white", fg="white")
    btn_w5_makeindimg.grid(row=5, column=5, sticky=W + E + N + S)

    btn_w5_maketable = Button(neowindow5, text="장표", bg="white", fg="white", width=20)
    btn_w5_maketable.grid(row=11, column=5, sticky=W + E + N + S)


    pass



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
        text_screen_big.insert(END,f'{"{0:0=4}".format(ind + 1)}. {"{" ":30}".format(i[0:i.index(":") - 1])} {i[i.index(":") + 2:len(i) - 1]}\n')
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

btn_openneowindow3 = Button(root, text="사진만들기", width=20, command=openneowindow4)
btn_openneowindow3.grid(row=3, column=7,sticky=N+W+E+S)

btn_openneowindow5 = Button(root, text="chemsketch", width=20, command=openneowindow5)
btn_openneowindow5.grid(row=4, column=7,sticky=N+W+E+S)

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