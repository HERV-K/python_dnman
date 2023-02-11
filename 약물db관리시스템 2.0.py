import os
import glob

from tkinter import ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont, ImageTk
import cv2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from urllib.request import urlopen
import pyautogui as pygui
from functools import partial
import math
#cf. 메모장
#셀레늄으로 크롤링할 때 해당 약물 창 안나오는 애는 txt 파일에 Acetaminophen : PASS 로 나타나게 하고
# 나중에 smile서 구조 그릴 때 PASS인 녀석은 빼는 걸로,,

#### 사진 긁어오기 할 때 사진폴더에 있는 사진에 대해서는  PASS 시전하는 코드 필요

global listofsubs
listofsubs = ["Pharmacology_katsung", "Medicinal chemistry", "Antibiotics"]

#1. 과목 폴더 규칙
#1.1 구성
    # 과목폴더명_tableofcontents 폴더에 과목의 목차를 정리해둔다. 
    # 과목폴더에 들어갔을 때 txt 파일은 위 파일 하나여야 한다.
    # 폴더의 이름은 01. ㅇㅇㅇ    의 형식을 지킨다.




#1. 메인 창
#1.1 메인창 생성
root = Tk()
root.title("drug db management system")
root.geometry("1000x500+100+50")
#1.2 기본함수 정의
#1.2.0 txt 가져오기
def getdictfromtxt(pathurl, splitsymbol):
    dict1 = {}
    file_opened = open(pathurl, "r", encoding="utf8")
    lines = file_opened.readlines()
    for ind, i in enumerate(lines):
        dict1[i[0:i.index(str(splitsymbol))]] = i[i.index(str(splitsymbol))+len(splitsymbol):i.index("\n")]
    file_opened.close()
    # print(dict1)
    return dict1
        
# getdictfromtxt(r"C:\OneDrive\DDB\Pharmacology_katsung\Pharmacology_katsung_tableofcontents.txt", ". ")
# db 읽어오려면,,  getdictfromtxt(r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt", " : ")

#1.2.1 폴더에 들어있는 폴더, 파일명 가져오기
def getlistfrompathurl(pathurl):
    folderslist = os.listdir(pathurl)
    return folderslist

def getlistfrompathurl2(pathurl):
    folderslist = os.listdir(pathurl)
    folderslist2 = []
    for ind, i in enumerate(folderslist):
        #이 for문은,, 01. alcohol 같은 경우 1을, 111 같은 경우 111을, ㅁㅇㄴㄹ 의 경우 건너뛰고 리스트에 append
        if str(i).count(r". ") == 1:
            folderslist2.append(int(i[0:str(i).rfind(". ")]))
        elif str.isdigit(i) == True:
            folderslist2.append(i)
        else:
            folderslist2.append(" ")
    return folderslist2
            
#1.2.2 폴더존재여부확인 - 입력한 이름의 폴더 있는지 확인하고 없으면 생성
def checkfolderpath(pathurl, foldernomen):
    pathtocheck = pathurl + f"\{foldernomen}"
    if os.path.exists(pathtocheck) == True:
        pass
    else:
        os.mkdir(path = pathtocheck)

#1.2.3 att의 경로의 txt파일을 기반으로 파일의 이름(숫자)에 목차명을 더해 반환한다.
def deffilename(pathurl, pathurloftxt, format):
    #pathurl은 파일폴더명을 변경할 녀석들이 들어있는 폴더의 url
    #pathruloftxt는 참고할 목차 txt파일
    #filetorename은 이름 바꿀 파일
    dict1 = getdictfromtxt(pathurloftxt, ". ")  # 목차 txt서 불러오기
    folderslist = getlistfrompathurl(pathurl)
    #개명할 파일 번호에 해당하는 숫자가 dict1에 없다면 pass
    #있으면 
    #3. 폴더서 숫자만 추출해 리스트 생성
    folderslist2 = []
    for ind, i in enumerate(folderslist):
        #이 for문은,, 01. alcohol 같은 경우 1을, 111 같은 경우 111을, ㅁㅇㄴㄹ 의 경우 건너뛰고 리스트에 append
        if str(i).count(r". ") == 1:
            folderslist2.append(int(i[0:str(i).rfind(". ")]))
        elif str.isdigit(i) == True:
            folderslist2.append(i)
        else:
            pass
    print(f"해당 과목의 폴더에 있는 숫자관련 문자열은 {folderslist2} 이 있다.")    
    dict2 = {}
    for ind, i in enumerate(folderslist2):
        if i in list(dict1.keys()):
            dict2[int(i)] = dict1['{0:0=2}'.format(int(i))]
    print(f"dict2 {dict2}")

    for ind, i in enumerate(dict2.keys()):
        PATH1 = pathurl
        if len(format) ==0:
            PATH2 = PATH1 + f"\{'{0:0=2}'.format(i)}"
            filename =PATH1+ f"\{'{0:0=2}'.format(i)}. {dict2[i]}"
        else:
            PATH2 = PATH1 + f"\{'{0:0=2}'.format(i)}.{format}"
            filename =PATH1 + f"\{'{0:0=2}'.format(i)}. {dict2[i]}.{format}"
        
        print(f"filename은 {filename}")
        os.rename(PATH2, filename)

#1.2.4 입력창에 입력한 숫자에 목차txt의 목차를 덧댄 이름을 반환한다.
def getnamefromtoc(pathurloftxt, numb):
    #pathurloftxt는 목차 txt의 경로
    #numb는 입력창서 받아온 숫자
    #목차txt를 읽어 딕셔너리를 받아온다. 
    dict1 = getdictfromtxt(pathurloftxt, ". ")
    num1 = '{0:0=2}'.format(int(numb))
    filefullname = f"{'{0:0=2}'.format(int(numb))}. {dict1[num1]}"
    return filefullname

# getnamefromtoc(r"C:\OneDrive\DDB\Pharmacology_katsung\Pharmacology_katsung_tableofcontents.txt", 1)
# deffilename(r"C:\OneDrive\DDB\Pharmacology_katsung", r"C:\OneDrive\DDB\Pharmacology_katsung\Pharmacology_katsung_tableofcontents.txt", "")


#1.3 새 윈도우 만들기
#1.3.1 윈도우1 - 약물명plu 입력창
def openneowindow1():
    #1.3.1.1 윈도우1 생성
    global neowindow1
    neowindow1 = Toplevel(root)
    neowindow1.geometry("1200x800+100+100")

    #1.3.1.2 윈도우1 기초 레이아웃
    label_w1_top = Label(neowindow1, text="폴더 이름을 입력하세요")
    label_w1_top.grid(row=1,column=1,columnspan=5,sticky=N+W+E+S)
    ent_w1_newfilename = Entry(neowindow1)
    ent_w1_newfilename.grid(row=2,column=1,columnspan=4,sticky=N+W+E+S)
    scrollbar_w1_text = Scrollbar(neowindow1)
    scrollbar_w1_text.grid(row=10,column=10, rowspan = 5,sticky=N+W+E+S)
    text_w1_input = Text(neowindow1)
    text_w1_input.grid(row=10,column=6,columnspan=4, rowspan = 5,sticky=N+W+E+S)
    scrollbar_w1_text.config(command=text_w1_input.yview)

    #1.3.1.3 콤보박스들
    global listofsubs
    combox_w1_sub = ttk.Combobox(neowindow1, values=listofsubs)
    combox_w1_sub.current(0)
    combox_w1_sub.grid(row=2,column=5,sticky=N+W+E+S)


    #1.3.1.4 폴더 경로 확인 및 생성 버튼
    #이 함수는,, 과목폴더 안에 입력한 단원(int)에 대응하는 폴더가 있는지 확인할 것이다.    
    def checkfileandfolders(pathurl, foldernomen, foldernomen2):
        btn_w1_getdrugnames.config(bg="black")
        btn_w1_getdrugnames.update()
        #1. url지정
        foldernomen2 = int(foldernomen2.get())
        print(f"foldernomen2 = {foldernomen2}")
        foldernomen = foldernomen.get()
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"

        #2. 지정한 url에 있는 폴더 가져오기
        folderslist = getlistfrompathurl(PATH2)
        print(f"경로 {PATH2}에는 {folderslist}")

        #3. 폴더서 숫자만 추출해 리스트 생성
        folderslist2 = getlistfrompathurl2(PATH2)
        print(f"해당 과목의 폴더에 있는 숫자관련 문자열은 {folderslist2} 이 있다.")
        #4. 리스트에 입력한 폴더명 없으면 check1이 1이 됨
        check1 = 0
        #folderslist2에서 빈칸이 나오면 int오류가 난다..
        folderslist3 = []
        for ind, i in enumerate(folderslist2):
            if i == " ":
                pass
            else:
                folderslist3.append(i)
        
        if folderslist2 == [" "]:
            check1 = 1
        else:
            for ind, i in enumerate(folderslist3):
                if int(str(i)) == int(str(foldernomen2)):
                    print(int(str(i)))
                    check1 = 0
                    PATH5 = PATH2 + f"\{folderslist[ind]}"
                    PATH6 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
                    os.rename(PATH5, PATH6)
                    break
                else:
                    check1 = 1
            print(f"ckeck1(입력값에 해당하는 숫자가 폴더내 파일 숫자 리스트에 있으면 0, 아님 1) = {check1}")
            
        #5. check1이 1이면 폴더를 생성
        if check1 == 1:
            PATH3 = PATH2 + f'\{getnamefromtoc(txturl, foldernomen2)}'
            print(getnamefromtoc(txturl, foldernomen2))
            os.mkdir(path = PATH3)
            print(f"대응하는 폴더가 없으므로 폴더를 생성함")
        else:
            print(f"폴더 있으니 넘어감")
            print("###")
            print("###")
            print("###")
            print("###")
            print("###")
                
    btn_w1_maketxt = Button(neowindow1, text = "파일폴더 검사", command=partial(checkfileandfolders, r"C:\OneDrive\DDB", combox_w1_sub, ent_w1_newfilename))
    btn_w1_maketxt.grid(row=3,column=1,columnspan=4,sticky=N+W+E+S)

    #1.3.1.5 텍스트창에 입력한 약물 txt에 옮기기
    label_w1_txtfilename = Label(neowindow1, text="txt명을 입력하세요")
    label_w1_txtfilename.grid(row=4,column=1,columnspan=5,sticky=N+W+E+S)

    ent_w1_txtname = Entry(neowindow1)
    ent_w1_txtname.grid(row=5,column=1,columnspan=4,sticky=N+W+E+S)

    def getinputnames(pathurl, foldernomen, foldernomen2):
        #foldernomen은 과목명
        #0. 경로설정
        #입력한 경로(숫자)에 txt파일서 덧쓴 폴더명을 받아와야 하며
        #txt파일의 경우 생성 후 위 과정 반복,,
        foldernomen2 = int(foldernomen2.get())
        foldernomen = foldernomen.get()
        # txtfilenomen = int(txtfilenomen.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2 + f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"

        #1. 해당 챕터 폴더 내의 폴더 및 파일 리스트화
        folderslist = os.listdir(PATH3)
        folderslist2 = getlistfrompathurl2(PATH3)
        # print(folderslist, folderslist2)

        #2. txt 있나 확인
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        if txtnametohave in folderslist:
            #2.1 해당 txt가 있으면
            pass
        else:
            #2.2 txt가 없으면,, 만들어야
            PATHTXT = PATH3 + f"\{txtnametohave}"
            file_opened = open(PATHTXT, "w", encoding="utf8")
            file_opened.close()
        
        #3. 약물 이름을 리스트화
        # print("입력한 약물들입니다. \n",text_w1_input.get("1.0", "end").replace("\n","|"))
        listofinputname = text_w1_input.get("1.0", "end").replace("\n","|").split("|")
        listofinputname = listofinputname[:-1]
        
        #3.1 약물 이름 대문자화
        listofinputname2 = []
        for ind, i in enumerate(listofinputname):
            drugname = str(i[0].upper())+str(i[1:len(i)])
            listofinputname2.append(drugname)
        print(f"입력한 약물은 {listofinputname2} 입니다.")

        #4. txt파일에 입력
        PATHTXT = PATH3 + f"\{txtnametohave}"
        file_opened = open(PATHTXT, "a", encoding="utf8")
        listsorted = sorted(listofinputname2)
        for ind, i in enumerate(listsorted):
            file_opened.write(f"{i} : \n")
        file_opened.close()


    btn_w1_getdrugnames = Button(neowindow1, text="입력한 약물 txt로", bg="white", fg="white", \
         command=partial(getinputnames,r"C:\OneDrive\DDB", combox_w1_sub, ent_w1_newfilename))
    btn_w1_getdrugnames.grid(row=16,column=6,sticky=N+W+E+S)

    #1.3.1.6 smiles 가져오기
    def getsmiles(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        PATH1 = pathurl
        foldernomen = foldernomen.get()
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2 + f"\{foldernomen}_tableofcontents.txt"
        foldernomen2 = int(foldernomen2.get())
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"

        #2. 텍스트 불러오기
        dict1 = getdictfromtxt(PATHTXT, " : ")
        tofindlist = list(dict1.keys())
        print(f"dict1은 {dict1} 입니다.")
        print(f"tofindlist는 {tofindlist} 입니다.")
        dict11 = {}
        #3. : PASS 인 녀석 빼기
        dict2 = {}
        for ind, i in enumerate(tofindlist):
            if dict1[i] == "PASS":
                pass
            elif dict1[i] != "":
                dict11[i] = dict1[i]
                pass
            else:
                dict2[i] = i
                dict11[i] = dict1[i]

        #4. smile 가져오기
        browser = webdriver.Chrome()
        # browser.maximize_window()
        url = "https://go.drugbank.com/"
        listtofind = list(dict2.keys())
        listtofind2 = list(dict11.keys())
        print(f"listtofind는 {listtofind} 입니다.")
        print(f"dict11은 {dict11} 입니다.")
        print(f"listtofind2는 {listtofind2} 입니다.")
        print("###########################################################################################################")
        text_screen_big.delete("1.0", END)
        smilelist = []
        for i in listtofind:
            browser.get(url)
            searchtab = browser.find_element(By.CLASS_NAME, "search-query")
            searchtab.send_keys(i)
            button = browser.find_element(By.CLASS_NAME, "input-group-append")
            button.click()

            parent = browser.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[1]")
            
            tester1 = len(parent.find_elements(By.TAG_NAME, "h1"))
            if tester1 ==0:
                text_screen_big.insert(END, f"{i}\n")
                smilelist.append("ERROR")
                print(f"{i} 는 데이타베이스에 없거나 오타가 났을 것입니다...")
            else:
                parent = browser.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[2]/dl[6]")
                dt = parent.find_elements(By.TAG_NAME, "dt")
                dd = parent.find_elements(By.TAG_NAME, "dd")
                checklist = []
                for ind, inn in enumerate(dt):
                    checklist.append(inn.text)

                if "SMILES" in checklist:
                    listdttxt = []
                    for ind in dt:
                        listdttxt.append(ind.text)
                    listddtxt = []
                    for ind in dd:
                        listddtxt.append(ind.text)
                    dtd = list(zip(listdttxt, listddtxt))
                    smilelist.append(dtd[len(dtd) - 1][1])
                    print(f"{i}의 SMILES는 {dtd[len(dtd) - 1][1]} 입니다.")
                    
                else:
                    text_screen_big.insert(END, f"{i}\n")
                    smilelist.append("ERROR")
                    print(f"{i}는 저분자화합물이 아닌 듯 합니다...")
        nameandsmile = list(zip(listtofind, smilelist))


        dict_smiles = {}
        for ind, i in enumerate(listtofind):
            dict_smiles[i] = nameandsmile[ind][1]
        print("###############################################################################################################")
        print("결과 리스트(dict_smiles) : ", dict_smiles)

        #6. txt에 저장
        file_opened = open(PATHTXT, "w", encoding="utf8")
        dict_PASS = {}
        dict_OLD = {}
        dict_ERROR = {}
        dict_SMILES = {}


        for ind, i in enumerate(tofindlist):
            if i not in listtofind2: #PASS
                dict_PASS[i] = "PASS"
            elif i in listtofind2 and i not in listtofind: # 옛날부터 있던애
                dict_OLD[i] = dict11[i]
            elif i in listtofind:
                dict_SMILES[i] = dict_smiles[i]
            else:
                pass
        


        # for ind, i in enumerate(tofindlist):
        #     if i not in list(dict11.keys()): # PASS인 애
        #         dict_PASS[i] = "PASS"
        #     elif dict_smiles[i] == "ERROR": #ERROR인 애
        #         dict_ERROR[i] = "ERROR"
        #     else:
        #         dict_SMILES[i] = dict_smiles[i]
        
        dict3 = {**dict_OLD, **dict_SMILES, **dict_PASS, **dict_ERROR}
        dict4 = {}
        list2 = sorted(list(dict3.keys()))
        for ind, i in enumerate(list2):
            dict4[i] = dict3[i]
        print(f"dict4 는 {dict4} 입니다. txt에 쓰겠읍니다.")
        for code, name in dict4.items():
            file_opened.write(f"{code} : {name}\n")
        file_opened.close()

    btn_w1_getsmile = Button(neowindow1, text="smiles",command=partial(getsmiles,r"C:\OneDrive\DDB", combox_w1_sub, ent_w1_newfilename))
    btn_w1_getsmile.grid(row=16,column=7,sticky=N+W+E+S)

    def getdrugnamesformfolder(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        foldernomen = foldernomen.get()
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. 폴더내 리스트 가져오기
        list1 = os.listdir(PATH4)

        #3. list1 중에서 png 파일만 가져오기
        list2 = [] # list2는 사진 파일 이름 중의 약물이름이다.
        for ind, i in enumerate(list1):
            if i[i.index(".")+1:len(i)] == "png":
                list2.append(i[0:i.index(".")])
        return list2

    #1.3.1.7 smile서 구조 얻기
    def getstrimg(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        PATH1 = pathurl
        foldernomen = foldernomen.get()
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2 + f"\{foldernomen}_tableofcontents.txt"
        foldernomen2 = int(foldernomen2.get())
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        checkfolderpath(PATH3, foldernametohave)
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. 경로에 사진 폴더 생성하기
        
        

        #3. 구조 가져올 txt 열기
        dict1 = getdictfromtxt(PATHTXT, " : ")
        print("dict1은 ",dict1)

        #3.5 사진폴더에 이름 있는 놈들은 제끼기
        list3 = getdrugnamesformfolder(r"C:\OneDrive\DDB", combox_w1_sub, ent_w1_newfilename)

        #4. dict1에서 smile 있는 놈만 추출
        dict2 = {}  # dict2는,, dict1서 smile 있는 놈만 추출한 딕셔너리
        for ind, i in enumerate(dict1.keys()):
            if dict1[i] == "PASS":
                pass
            elif dict1[i] == "ERROR":
                pass
            else:
                dict2[i] = dict1[i]
        print("dict2는 ", dict2)
        list1 = list(dict2.values())
        list2 = list(dict2.keys())
        print("list1은 ", list1)

        list5 = []
        list6 = []
        for ind, i in enumerate(list2):
            if i not in list3:
                list5.append(list1[ind])
                list6.append(i)




        #5. 구조 가져오기
        browser = webdriver.Chrome()
        # browser.maximize_window()
        url = "http://cdb.ics.uci.edu/cgibin/Smi2DepictWeb.py"
        browser.get(url)
        searchtab = browser.find_element(By.ID, "smiles")
        searchtab.clear()

        for i in list5:
            searchtab.send_keys(i)
            searchtab.send_keys(Keys.RETURN)

        btn = browser.find_element(By.XPATH, '//*[@id="Smi2DepictWeb"]/div[1]/div[5]/button')
        btn.click()
        time.sleep(2)
        img3 = browser.find_elements(By.CLASS_NAME, "shadow")

        for index, image in enumerate(img3):
            src = image.get_attribute("src")
            t = urlopen(src).read()
            file = open(os.path.join(PATH4, f"{list6[index]}.png"), "wb")
            file.write(t)
            print(list6[index])
        browser.close()

    btn_w1_getstrimg = Button(neowindow1, text="구조",command=partial(getstrimg,r"C:\OneDrive\DDB", combox_w1_sub, ent_w1_newfilename))
    btn_w1_getstrimg.grid(row=17,column=7,sticky=N+W+E+S)

def openneowindow3():
    global neowindow3
    neowindow3 = Toplevel(root)
    neowindow3.geometry("1200x600+100+100")

    label_w3_top = Label(neowindow3, text="폴더 이름을 입력하세요")
    label_w3_top.grid(row=1,column=1,columnspan=5,sticky=N+W+E+S)
    ent_w3_newfilename = Entry(neowindow3)
    ent_w3_newfilename.grid(row=2,column=1,columnspan=4,sticky=N+W+E+S)

    def multipleyviw(*args):
        text_w3_engname.yview(*args)
        text_w3_korname.yview(*args)

    scrollbar_w3_engname = Scrollbar(neowindow3)
    scrollbar_w3_engname.grid(row=10,column=8, rowspan = 5,sticky=N+W+E+S)

    text_w3_engname = Text(neowindow3, width= 30, yscrollcommand=scrollbar_w3_engname.set, wrap = "none" )
    text_w3_engname.grid(row=10,column=6,columnspan=2, rowspan = 5,sticky=N+W+E+S)
    text_w3_korname = Text(neowindow3, width= 30, yscrollcommand=scrollbar_w3_engname.set, wrap = "none" )
    text_w3_korname.grid(row=10,column=9,columnspan=2, rowspan = 5,sticky=N+W+E+S)
    
    scrollbar_w3_engname.config(command=multipleyviw)

    global listofsubs
    combox_w3_sub = ttk.Combobox(neowindow3, values=listofsubs)
    combox_w3_sub.current(0)
    combox_w3_sub.grid(row=2,column=5,sticky=N+W+E+S)
    #2. 사진 분자명 가져오기
    def getdrugnamesformfolder(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        # foldernomen = foldernomen.get()
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. 폴더내 리스트 가져오기
        list1 = os.listdir(PATH4)

        #3. list1 중에서 png 파일만 가져오기
        list2 = [] # list2는 사진 파일 이름 중의 약물이름이다.
        for ind, i in enumerate(list1):
            if i[i.index(".")+1:len(i)] == "png":
                list2.append(i[0:i.index(".")])
        return list2
    #3. 한영 비교
    def compareengetkor(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. 이름 가져오기
        print("namelist는  " , namelist, "입니다.")

        #3. db 가져오기
        PATHDB = r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt"
        dict_db = getdictfromtxt(PATHDB," : ")
        # print(f"dict_db는 {dict_db} 입니다.")

        #4. 챕터내 약물명 db와 비교
        dict3 = {}
        for ind, i in enumerate(namelist):
            if i in list(dict_db.keys()):
                dict3[i] = dict_db[i]
            else:
                dict3[i] = ""
                pass
        print(f"dict3는 {dict3} 입니다.")

        #5. txt박스에 입력하기
        #5.1 영어
        text_w3_engname.delete("1.0",END)
        for ind, i in enumerate(dict3.keys()):
            text_w3_engname.insert(END, f"{str(i)}\n")

        #5.2 한글
        text_w3_korname.delete("1.0",END)
        for ind, i in enumerate(dict3.values()):
            text_w3_korname.insert(END, f"{str(i)}\n")

    btn_w3_maketxt = Button(neowindow3, text = "파일폴더 검사", command=partial(compareengetkor, r"C:\OneDrive\DDB", combox_w3_sub, ent_w3_newfilename))
    btn_w3_maketxt.grid(row=3,column=1,columnspan=4,sticky=N+W+E+S)
    #4. 입력한 한국명 DB에 입력
    def getinput(pathurl, foldernomen, foldernomen2):
        #1. 경로
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        PATHDB = r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt"
        dict_db = getdictfromtxt(PATHDB," : ")

        #2. 텍박스 내용 가져오기

        eng = text_w3_engname.get("1.0", END).replace("\n","|").split("|")
        eng = eng[:-2]
        kor = text_w3_korname.get("1.0", END).replace("\n","|").split("|")
        kor = kor[:-2]

        print(eng, kor)
        #3. db 딕셔너리에 추가
        for ind, i in enumerate(eng):
            dict_db[i] = kor[ind]

        #4. db 정렬
        dict_edited = {}
        for ind, i in enumerate(sorted(dict_db.keys())):
            dict_edited[i] = dict_db[i]
        print(dict_edited)

        #5. db 텍스트 화일에 쓰기
        db_opened = open(PATHDB, "w", encoding="utf8")
        for code, name in dict_edited.items():
            db_opened.write(f'{code} : {name}\n')
        db_opened.close
        msgbox.showinfo("무챠쵸~", "Nomen tibi Pagayaro est.")

    btn_w3_getnames = Button(neowindow3, text="smiles",command=partial(getinput,r"C:\OneDrive\DDB", combox_w3_sub, ent_w3_newfilename))
    btn_w3_getnames.grid(row=16,column=7,sticky=N+W+E+S)

def openneowindow4():
    global neowindow4
    neowindow4 = Toplevel(root)
    neowindow4.geometry("1200x700+100+100")

    label_w4_top = Label(neowindow4, text="폴더 이름을 입력하세요")
    label_w4_top.grid(row=1,column=1,columnspan=5,sticky=N+W+E+S)
    ent_w4_newfilename = Entry(neowindow4)
    ent_w4_newfilename.grid(row=2,column=1,columnspan=4,sticky=N+W+E+S)

    scrollbar_w4_text = Scrollbar(neowindow4)
    scrollbar_w4_text.grid(row=10,column=10, rowspan = 5,sticky=N+W+E+S)
    text_w4_screen = Text(neowindow4, width=30)
    text_w4_screen.grid(row=10,column=6,columnspan=4, rowspan = 5,sticky=N+W+E+S)
    scrollbar_w4_text.config(command=text_w4_screen.yview)

    global listofsubs
    combox_w4_sub = ttk.Combobox(neowindow4, values=listofsubs)
    combox_w4_sub.current(0)
    combox_w4_sub.grid(row=2,column=5,sticky=N+W+E+S)

    #2. 사진 분자명 가져오기
    def getdrugnamesformfolder(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        # foldernomen = foldernomen.get()
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. 폴더내 리스트 가져오기
        list1 = os.listdir(PATH4)

        #3. list1 중에서 png 파일만 가져오기
        list2 = [] # list2는 사진 파일 이름 중의 약물이름이다.
        for ind, i in enumerate(list1):
            if i[i.index(".")+1:len(i)] == "png":
                list2.append(i[0:i.index(".")])
        return list2

    #3. 선택한 과목의 챕터 사진폴더 한글명유무 검사
    def selectfolder(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"

        #2. db 가져오기
        PATHDB = r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt"
        dict_db = getdictfromtxt(PATHDB," : ")
        # print(f"dict_db는 {dict_db} 입니다.")

        #3. 챕터내 약물명 db와 비교 : db에 있는 애만 dict3에 넣는다.
        dict3 = {}
        for ind, i in enumerate(namelist):
            if i in list(dict_db.keys()):
                dict3[i] = dict_db[i]
            else:
                dict3[i] = ""
                pass
        print(f"dict3는 {dict3} 입니다.")

        #4. dict3 value 중 ""이 있으면 오류 메시지를 띄우고 텍스트창에 오류 약물명을 입력한다.
        text_w4_screen.delete("1.0", END)
        check_w4_1 = 0
        text_w4_screen.insert(END, "*오류*오류*오류선생*오류*오류* : 한글명이 없는 약물이 아래와 같읍니다.\n")
        for ind, i in enumerate(dict3.values()):
            if i == "":
                text_w4_screen.insert(END, f"{list(dict3.keys())[ind]}\n")
                check_w4_1 +=1
            else:
                pass
        
        if check_w4_1 == 0:
            text_w4_screen.delete("1.0", END)
            text_w4_screen.insert(END, f"이상 無,, 작업을 진행하십쇼...")
            print("해당과목챕터에는 이상이 없읍니다...")
        else:
            text_w4_screen.update()
            print(text_w4_screen.get("1.0", END))
            time.sleep(0.5)
            neowindow4.destroy()

    btn_w4_maketxt = Button(neowindow4, text = "파일폴더 검사", command=partial(selectfolder, r"C:\OneDrive\DDB", combox_w4_sub, ent_w4_newfilename))
    btn_w4_maketxt.grid(row=3,column=1,columnspan=4,sticky=N+W+E+S)

    #4. 옵션창
        #4.1 글자 색상
    fontcolourlist = ["폰트색(기본 : 파)", "red", "yellow", "green", "blue", "black"]
    combox_w4_fontcol = ttk.Combobox(neowindow4, values=fontcolourlist,width=15, state="readonly")
    combox_w4_fontcol.current(0)
    combox_w4_fontcol.grid(row=2, column=6, sticky=W + E + N + S)

        #4.2 글자체
    fontlist = ["폰트(기본 : 쿠키런)", "쿠키런", "천년", "우리금융", "한바탕"]
    combox_w4_font = ttk.Combobox(neowindow4, values=fontlist,width=15, state="readonly")
    combox_w4_font.current(0)
    combox_w4_font.grid(row=3, column=6, sticky=W + E + N + S)

        #4.3 각개파일 해상도
    listofindimgsize = ["800x800","400x400", "자율"]
    combox_w4_indimgsize = ttk.Combobox(neowindow4,width=15,values = listofindimgsize)#, state="readonly")
    combox_w4_indimgsize.current(0)
    combox_w4_indimgsize.grid(row=2, column=7, sticky=W + E + N + S)

        #4.4 테이블 레이아웃
    layoutlist = ["5x6","4x5","4x4", "5x5","6x6", "5x7", "자율"]
    combox_w4_layout = ttk.Combobox(neowindow4,width=15, values = layoutlist)#, state = "readonly")
    combox_w4_layout.current(0)
    combox_w4_layout.grid(row=3, column=7, sticky=W + E + N + S)

        #4.5 약물명 포함여부
    Yesorno = ["약품명 포함?(예)", "예", "아니오"]
    combox_w4_contkor = ttk.Combobox(neowindow4,width=15, values=Yesorno, state="readonly")
    combox_w4_contkor.current(0)
    combox_w4_contkor.grid(row=2, column=8, sticky=W + E + N + S)


    #5. 생성함수들 및 버튼
    #5.1 폴더 내 이미지 가져오는 함수
    def getimgsfromfolder(pathurl, foldernomen, foldernomen2):
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"
        PATH5 = PATH3 + f"\{foldernametohave}" + r"\\"
        
        
        listofimgs = glob.glob(PATH5+"*.png")
        return listofimgs
        # img9 = Image.open(listofimgs[1])
        # img9.show()

    #5.2 리스트 내 이미지의 크기를 변경해 새로운 리스트로 반환하느 함수
    def changeimgsize(listtochange, sizelist):
        list_tochange = listtochange
        list_size = sizelist
        
        to_wid = int(list_size[0])
        to_hei = int(list_size[1])
        to_widheiratio = float(to_wid/to_hei)
        # print(f"변경할 사이즈는 {to_wid} x {to_hei} 입니다. ratio는 {to_widheiratio} 입니다.")
        #이미지 크기 변경 for문
        resultlist = []
        for ind, i in enumerate(list_tochange):
            #1.1. 이미지를 열고 크기를 알려준다.
            img = Image.open(i)
            img_wid = int(img.size[0])
            img_hei = int(img.size[1])
            img_widheiratio = float(img_wid/img_hei)

            # print(f"{ind}번 이미지의 사이즈는 {img_wid} x {img_hei} 입니다,,\
            #     이 이미지의 ratio는 {img_widheiratio} 입니다.")
            if img_widheiratio >= to_widheiratio:
                #1.2.1 처리할 이미지의 ratio가 기준 ratio보다 클 경우
                resultwid = to_wid
                resulthei = int(math.floor(to_wid/img_widheiratio))
                img2 = img.resize((resultwid,resulthei))
                # print(f"이 녀석은 결국 {resultwid} x {resulthei} 가 되었네영")
                resultlist.append(img2)
            else:
                #1.2.2 반대
                resultwid = int(math.floor(to_hei*img_widheiratio))
                resulthei = to_hei
                img2 = img.resize((resultwid,resulthei))
                # print(f"이 녀석은 결국 {resultwid} x {resulthei} 가 되었네영")
                resultlist.append(img2)
        return resultlist
        print("크기 변경 완료")
    # changeimgsize(getimgsfromfolder(r"C:\OneDrive\DDB", combox_w4_sub, ent_w4_newfilename), [1,2])
    
    def calculategoodsize(eng, kor, wid_box, hei_box, font, ind):

        Stextinbox_eng = eng
        Stextinbox_kor = kor
        Sfont_font = font
        Stxtbox_wid = wid_box
        Stxtbox_hei = hei_box
        len_engname = len(Stextinbox_eng)
        len_korname = len(Stextinbox_kor)
        # print(f"Stxtbox = {Stxtbox_wid}x{Stxtbox_hei}")

        temp_fontsize_eng = int(Stxtbox_hei/4)
        temp_fontsize_kor = int(Stxtbox_hei/4)
        temp_fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_eng)
        temp_fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_kor)
        temp_wid_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[2]
        temp_wid_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[2]
        temp_hei_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[3]
        temp_hei_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[3]
        temp_wid_margin = Stxtbox_wid - max(temp_wid_engbox, temp_wid_korbox)
        temp_hei_margin = Stxtbox_hei - (temp_hei_engbox+temp_hei_korbox)
        linewid = int(int(Stxtbox_wid)/200)
        var1 = math.floor(linewid/2)
        

        # print(f"변경전{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {temp_wid_engbox} x {temp_hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {temp_wid_korbox} x {temp_hei_korbox}                          {max(temp_wid_engbox, temp_wid_korbox)} x {temp_hei_engbox+temp_hei_korbox}, margin is {temp_wid_margin}x{temp_hei_margin}")

        if temp_wid_margin > 2*linewid and temp_hei_margin >2*linewid:
            while temp_wid_margin >6*linewid and temp_hei_margin >4*linewid:
                temp_fontsize_eng += var1
                temp_fontsize_kor += var1
                temp_fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_eng)
                temp_fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_kor)
                temp_wid_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[2]
                temp_wid_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[2]
                temp_hei_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[3]
                temp_hei_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[3]
                temp_wid_margin = Stxtbox_wid - max(temp_wid_engbox, temp_wid_korbox)
                temp_hei_margin = Stxtbox_hei - (temp_hei_engbox+temp_hei_korbox)
                # print(f"{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {temp_wid_engbox} x {temp_hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {temp_wid_korbox} x {temp_hei_korbox}                          {max(temp_wid_engbox, temp_wid_korbox)} x {temp_hei_engbox+temp_hei_korbox}, margin is {temp_wid_margin}x{temp_hei_margin}")

        elif temp_wid_margin <=2*linewid and temp_hei_margin >2*linewid :
            while temp_wid_margin <=6*linewid:
                temp_fontsize_eng -= var1
                temp_fontsize_kor -= var1
                temp_fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_eng)
                temp_fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_kor)
                temp_wid_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[2]
                temp_wid_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[2]
                temp_hei_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[3]
                temp_hei_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[3]
                temp_wid_margin = Stxtbox_wid - max(temp_wid_engbox, temp_wid_korbox)
                temp_hei_margin = Stxtbox_hei - (temp_hei_engbox+temp_hei_korbox)
                # print(f"{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {temp_wid_engbox} x {temp_hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {temp_wid_korbox} x {temp_hei_korbox}                          {max(temp_wid_engbox, temp_wid_korbox)} x {temp_hei_engbox+temp_hei_korbox}, margin is {temp_wid_margin}x{temp_hei_margin}")


        elif temp_wid_margin >2*linewid and temp_hei_margin <=2*linewid :
            while temp_wid_margin >6*linewid and temp_hei_margin <=4*linewid:
                temp_fontsize_eng -= var1
                temp_fontsize_kor -= var1
                temp_fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_eng)
                temp_fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_kor)
                temp_wid_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[2]
                temp_wid_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[2]
                temp_hei_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[3]
                temp_hei_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[3]
                temp_wid_margin = Stxtbox_wid - max(temp_wid_engbox, temp_wid_korbox)
                temp_hei_margin = Stxtbox_hei - (temp_hei_engbox+temp_hei_korbox)
                # print(f"{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {temp_wid_engbox} x {temp_hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {temp_wid_korbox} x {temp_hei_korbox}                          {max(temp_wid_engbox, temp_wid_korbox)} x {temp_hei_engbox+temp_hei_korbox}, margin is {temp_wid_margin}x{temp_hei_margin}")


        elif temp_wid_margin <=2*linewid and temp_hei_margin <=2*linewid :
            while temp_wid_margin <=6*linewid and temp_hei_margin <=4*linewid:
                temp_fontsize_eng -= var1
                temp_fontsize_kor -= var1
                temp_fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_eng)
                temp_fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = temp_fontsize_kor)
                temp_wid_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[2]
                temp_wid_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[2]
                temp_hei_engbox = temp_fontstyle_eng.getbbox(Stextinbox_eng)[3]
                temp_hei_korbox = temp_fontstyle_kor.getbbox(Stextinbox_kor)[3]
                temp_wid_margin = Stxtbox_wid - max(temp_wid_engbox, temp_wid_korbox)
                temp_hei_margin = Stxtbox_hei - (temp_hei_engbox+temp_hei_korbox)
        # print(f"변경후{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {temp_wid_engbox} x {temp_hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {temp_wid_korbox} x {temp_hei_korbox}                          {max(temp_wid_engbox, temp_wid_korbox)} x {temp_hei_engbox+temp_hei_korbox}, margin is {temp_wid_margin}x{temp_hei_margin}")
        result = [temp_fontsize_eng, temp_fontsize_kor]
        return result

    #5.3 약물명 리스트를 받고,, 입력한 크기에 맞는 이미지를 생성한다. 그 이미지는 리스트로 반환한다.
    def maketextboximg(dictofdrugnames, sizelist, font, fontcol, drugnameYoN):
        #0. 이미지 제작에 실사용할 변수 먼저 정해둘 것..
        dict1 = dictofdrugnames
        size = sizelist
        font = font.get()
        fontcol = fontcol.get()
        YoN = drugnameYoN

        #1. 박스 크기 결정
        Stxtbox_wid = int(size[0])
        Stxtbox_hei = int(size[1])

        #2. 글자색 결정
        if fontcol == "red":
            Sfont_col = "RGBA(255, 051, 051, 255)"
        elif fontcol == "black":
            Sfont_col = "RGBA(000, 000, 000, 255)"
        elif fontcol == "yellow":
            Sfont_col = "RGBA(255, 204,000, 255)"
        elif fontcol == "green":
            Sfont_col = "RGBA(000, 153, 000, 255)"
        else:
            #기본색, 파란색임
            Sfont_col = "RGBA(000, 051, 255, 255)"
        
        #3. 폰트 설정
        if font == "천년":
            Sfont_font = r"C:\OneDrive\DDB\fonts\경기천년바탕_Regular.ttf"
        elif font == "한바탕":
            Sfont_font = r"C:\OneDrive\DDB\fonts\HANBatang.ttf"
        elif font == "우리금융":
            Sfont_font = r"C:\OneDrive\DDB\fonts\우리다움 R.ttf"
        else:
            #기본폰트, 쿠키런어쩌구임
            Sfont_font = r"C:\OneDrive\DDB\fonts\CookieRun Regular.ttf"
        
        #4. 기타 변수 설정
        global bgcolor
        Sbg = bgcolor
        # Stextinbox_kor - 한국 이름 > 이미지 만들기 들어가야 결정 가능,,
        # Stextinbox_eng - 영어 이름 > 이미지 만들기 들어가야 결정 가능,,
        # SkornameYoN - 한글 포함 여부
        # SPATHTABLESAVE - 테이블 저장경로
        # SPATHIMGSAVE - 개별이미지 저장경로


        #6. 텍스트 이미지 만들기
        resultboximg = [] # 생성한 이미지 담을 리스트
        dict1_keys = list(dict1.keys())
        dict1_values = list(dict1.values())
        print(Stxtbox_wid, Stxtbox_hei)

        for ind, i in enumerate(dict1_keys):
            #4.1 변수 설정
            Stextinbox_eng = dict1_keys[ind]
            Stextinbox_kor = dict1_values[ind]

            #5.1 파라메다 설정
            txtsizelist = calculategoodsize(Stextinbox_eng, Stextinbox_kor, Stxtbox_wid, Stxtbox_hei, Sfont_font, ind)
            len_engname = len(Stextinbox_eng)
            len_korname = len(Stextinbox_kor)
            fontsize_eng = int(txtsizelist[0])
            fontsize_kor = int(txtsizelist[1])
            fontstyle_eng = ImageFont.truetype(font = Sfont_font, size = fontsize_eng)
            fontstyle_kor = ImageFont.truetype(font = Sfont_font, size = fontsize_kor)
            wid_engbox = fontstyle_eng.getbbox(Stextinbox_eng)[2]
            wid_korbox = fontstyle_kor.getbbox(Stextinbox_kor)[2]
            hei_engbox = fontstyle_eng.getbbox(Stextinbox_eng)[3]
            hei_korbox = fontstyle_kor.getbbox(Stextinbox_kor)[3]
            wid_margin = Stxtbox_wid - max(wid_engbox, wid_korbox)
            hei_margin = Stxtbox_hei - (hei_engbox+hei_korbox)
            print(f"{'{0:0=4}'.format(ind)}. {Stextinbox_eng}: 길이는 {len_engname}, 박스크기는 {wid_engbox} x {hei_engbox}|{Stextinbox_kor} : 길이는 {len_korname}, 박스크기는 {wid_korbox} x {hei_korbox}                          {max(wid_engbox, wid_korbox)} x {hei_engbox+hei_korbox}, margin is {wid_margin}x{hei_margin}")

            #5.2 이미지 제작 시작

            if drugnameYoN == "N":
                x_engtxtbox = int((Stxtbox_wid - wid_engbox)/2)
                y_engtxtbox = int(hei_margin/2)
                x_kortxtbox = int((Stxtbox_wid - wid_korbox)/2)
                y_kortxtbox = y_engtxtbox + int(hei_engbox)

                textedimg = Image.new("RGBA",(Stxtbox_wid, Stxtbox_hei), color= bgcolor)
                draw = ImageDraw.Draw(textedimg)
                draw.rectangle(((0,0),(Stxtbox_wid,Stxtbox_hei)), outline="red", width=int(Stxtbox_wid/200))
                draw.text((x_engtxtbox, y_engtxtbox), " ", font = fontstyle_eng, fill = Sfont_col)
                draw.text((x_kortxtbox, y_kortxtbox), " ", font = fontstyle_kor, fill = Sfont_col)
                resultboximg.append(textedimg)
                
            else:
                x_engtxtbox = int((Stxtbox_wid - wid_engbox)/2)
                y_engtxtbox = int(hei_margin/2)
                x_kortxtbox = int((Stxtbox_wid - wid_korbox)/2)
                y_kortxtbox = y_engtxtbox + int(hei_engbox)

                textedimg = Image.new("RGBA",(Stxtbox_wid, Stxtbox_hei), color= bgcolor)
                draw = ImageDraw.Draw(textedimg)
                draw.rectangle(((0,0),(Stxtbox_wid,Stxtbox_hei)), outline="red", width=int(Stxtbox_wid/200))
                draw.text((x_engtxtbox, y_engtxtbox), Stextinbox_eng, font = fontstyle_eng, fill = Sfont_col)
                draw.text((x_kortxtbox, y_kortxtbox), Stextinbox_kor, font = fontstyle_kor, fill = Sfont_col)
                resultboximg.append(textedimg)
        return resultboximg





        #df
        #draw.rectangle((point1, point2), outline=(0, 0, 255), width=3)

    #개별이미지 만들기
    def makeindimgs(pathurl, foldernomen, foldernomen2):
        list_test = getimgsfromfolder(pathurl, foldernomen, foldernomen2)
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"
        PATH5 = PATH3 + f"\{foldernametohave}" + r"\\"


        #labeled img 폴더 확인하고 없으면 만들기
        nomennomen = f"{getnamefromtoc(txturl, foldernomen2)}_labeled"
        checkfolderpath(PATH3, nomennomen)
        PATH7 = os.path.join(PATH3, f"{str(nomennomen)}")



        #이름 영어, 한글 가져오기
        #2. db 가져오기
        PATHDB = r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt"
        dict_db = getdictfromtxt(PATHDB," : ")
        # print(f"dict_db는 {dict_db} 입니다.")

        #3. 챕터내 약물명 db와 비교 : db에 있는 애만 dict3에 넣는다.
        dict3 = {}
        for ind, i in enumerate(namelist):
            if i in list(dict_db.keys()):
                dict3[i] = dict_db[i]
            else:
                dict3[i] = ""
                pass
        # print(f"dict3는 {dict3} 입니다.")
        listdict3 = list(dict3.keys())

        #콤박스서 이미지 크기 가져오는 코드
        widthofimg = int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")])
        heightofimg = int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])
        # 텍스트이미지의 크기 결정
        #changeimgsize(list_test, [widthofimg,heightofimg])

        #텍스트부분 사진 만드는 함수 정의
        global bgcolor
        bgcolor = "RGBA(255,255,255,255)"

        #제작한 텍스트박스 리스트로 받아오기
        txtboxlist = maketextboximg(dict3, [widthofimg,int(heightofimg*3/8)], combox_w4_font, combox_w4_fontcol, "Y")
        # print(txtboxlist)

        #사진의 크기 변경 > 
        listofadjustedimg = changeimgsize(list_test, [widthofimg,int(heightofimg*5/8)])
        # print(namelist)
        # print(listofadjustedimg)

        listofwholeimg = []
        for i in range(0, len(txtboxlist)):
            resultimg = Image.new("RGBA", (widthofimg, heightofimg), color = bgcolor)
            photo = listofadjustedimg[i]
            txtbox = txtboxlist[i]
            wid = int(photo.size[0])
            hei = int(photo.size[1])
            ratio = float(wid/hei)
            ratio_critaria = float((8*widthofimg)/(5*heightofimg))
            widmargin = int((widthofimg-wid)/2)
            heimargin = int(((5*heightofimg/8)-hei)/2)

            if ratio >= ratio_critaria:
                resultimg.paste(photo,(0,heimargin))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
            else:
                resultimg.paste(photo,(widmargin,0))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
                
            listofwholeimg.append(resultimg)
            # resultimg.show()
            PATH8 = PATH7 + f"\{listdict3[i]}.png"
            resultimg.save(PATH8)


    def maketable(listofimgs, com_layout, sizelist):
        #경로
        listofimg = listofimgs
        layoutlist = com_layout.get()
        sizelist = sizelist
        wid = int(sizelist[0])
        hei = int(sizelist[1])

        #레이아웃 숫자
        columnnum = int(layoutlist[0:layoutlist.rfind("x")])
        rownum = int(layoutlist[layoutlist.rfind("x")+1:])
        print(f"칼럼은 {columnnum}개 , 로는 {rownum}개")
        pagenum = 1 + int(len(listofimg)/(columnnum*rownum))
        print(f"페이지수는 {pagenum} 입니다.")

        #페이지별 
        pagelist = []
        for a in range(1, pagenum+1):
            pagelist.append(f"page{a}")
            pagelist[a-1] = Image.new("RGBA", (wid*columnnum,hei*rownum), (255, 255, 255, 255))
            print(f"페이지번호 : {a}")
            for b in range(1, rownum+1):
                print(f"{a}번 페이지의 {b}번줄")
                for c in range(1, columnnum+1):
                    if columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b <= len(listofimg)-1:
                        print(f"{a}번 페이지의 {b}번줄의 {c}번 칼럼에는 {columnnum * rownum * (a - 1) + (columnnum + 1) * (b - 1) + c - b}가 들어간다.")
                        pagelist[a-1].paste(listofimg[int(columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b)], (wid*(c-1)-c+1, hei*(b-1)-b+1))

                    else:
                        break
                if columnnum*rownum*(a-1)+(columnnum+1)*(b-1)+c-b <= len(listofimg)-1:
                    pass
                else:
                    break
            if columnnum * rownum * (a - 1) + (columnnum + 1) * (b - 1) + c - b <= len(listofimg) - 1:
                pass
            else:
                break
        return pagelist

        # for ind, i in enumerate(pagelist):
        #     pathway_jpg = os.path.join(r"C:\OneDrive\Drug structure DB\Tables", f"table of {ent_w4_filename.get()}__{ind}.png")
        #     i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
        #     i.save(pathway_jpg)
        #     print("저장완료")


        


        pass

    def test2(pathurl, foldernomen, foldernomen2):
        #경로
        list_test = getimgsfromfolder(pathurl, foldernomen, foldernomen2)
        foldernomen = foldernomen.get()
        namelist = getdrugnamesformfolder(pathurl, foldernomen, foldernomen2)
        foldernomen2 = int(foldernomen2.get())
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2+f"\{foldernomen}_tableofcontents.txt"
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        PATH4 = PATH3 + f"\{foldernametohave}"
        PATH5 = PATH3 + f"\{foldernametohave}" + r"\\"


        #labeled img 폴더 확인하고 없으면 만들기
        nomennomen = f"{getnamefromtoc(txturl, foldernomen2)}_labeled"
        checkfolderpath(PATH3, nomennomen)
        PATH7 = os.path.join(PATH3, f"{str(nomennomen)}")



        #이름 영어, 한글 가져오기
        #2. db 가져오기
        PATHDB = r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt"
        dict_db = getdictfromtxt(PATHDB," : ")
        # print(f"dict_db는 {dict_db} 입니다.")

        #3. 챕터내 약물명 db와 비교 : db에 있는 애만 dict3에 넣는다.
        dict3 = {}
        for ind, i in enumerate(namelist):
            if i in list(dict_db.keys()):
                dict3[i] = dict_db[i]
            else:
                dict3[i] = ""
                pass
        # print(f"dict3는 {dict3} 입니다.")
        listdict3 = list(dict3.keys())

        #콤박스서 이미지 크기 가져오는 코드
        widthofimg = int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")])
        heightofimg = int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])
        sizelist = [widthofimg, heightofimg]
        # 텍스트이미지의 크기 결정
        #changeimgsize(list_test, [widthofimg,heightofimg])

        #텍스트부분 사진 만드는 함수 정의
        global bgcolor
        bgcolor = "RGBA(255,255,255,255)"

        #제작한 텍스트박스 리스트로 받아오기
        txtboxlist = maketextboximg(dict3, [widthofimg,int(heightofimg*3/8)], combox_w4_font, combox_w4_fontcol, "Y")
        txtboxlist_no = maketextboximg(dict3, [widthofimg,int(heightofimg*3/8)], combox_w4_font, combox_w4_fontcol, "N")
        # print(txtboxlist)

        #사진의 크기 변경 > 
        listofadjustedimg = changeimgsize(list_test, [widthofimg,int(heightofimg*5/8)])
        # print(namelist)
        # print(listofadjustedimg)

        #글자 있는 테이블 만들기
        listofwholeimg = []
        for i in range(0, len(txtboxlist)):
            resultimg = Image.new("RGBA", (widthofimg, heightofimg), color = bgcolor)
            photo = listofadjustedimg[i]
            txtbox = txtboxlist[i]
            wid = int(photo.size[0])
            hei = int(photo.size[1])
            ratio = float(wid/hei)
            ratio_critaria = float((8*widthofimg)/(5*heightofimg))
            widmargin = int((widthofimg-wid)/2)
            heimargin = int(((5*heightofimg/8)-hei)/2)

            if ratio >= ratio_critaria:
                resultimg.paste(photo,(0,heimargin))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
            else:
                resultimg.paste(photo,(widmargin,0))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
                
            listofwholeimg.append(resultimg)
        labeledtable = maketable(listofwholeimg, combox_w4_layout, sizelist)
            # resultimg.show()
            # PATH8 = PATH7 + f"\{listdict3[i]}.png"
            # resultimg.save(PATH8)
        #글자 없는 테이블 만들기
        listofwholeimg_no = []
        for i in range(0, len(txtboxlist_no)):
            resultimg = Image.new("RGBA", (widthofimg, heightofimg), color = bgcolor)
            photo = listofadjustedimg[i]
            txtbox = txtboxlist_no[i]
            wid = int(photo.size[0])
            hei = int(photo.size[1])
            ratio = float(wid/hei)
            ratio_critaria = float((8*widthofimg)/(5*heightofimg))
            widmargin = int((widthofimg-wid)/2)
            heimargin = int(((5*heightofimg/8)-hei)/2)

            if ratio >= ratio_critaria:
                resultimg.paste(photo,(0,heimargin))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
            else:
                resultimg.paste(photo,(widmargin,0))
                resultimg.paste(txtbox, (0,int(5*heightofimg/8)))
                
            listofwholeimg_no.append(resultimg)
        nonlabeledtable = maketable(listofwholeimg_no, combox_w4_layout, sizelist)
        labeledpdf = []
        for ind, i in enumerate(labeledtable):
            pathway_jpg = os.path.join(PATH3 ,f"table of {getnamefromtoc(txturl, foldernomen2)} {'{0:0=2}'.format(ind+1)}_Labled.png")
            # i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
            i.save(pathway_jpg)
            i2 = i.convert("RGB")
            labeledpdf.append(i2)
        pathway_pdf = os.path.join(PATH3 ,f"table of {getnamefromtoc(txturl, foldernomen2)}_Labled.pdf")
            # # i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
            # i2.save(pathway_pdf)
        imama = labeledpdf[0]
        labeledpdf.pop(0)
        imama.save(pathway_pdf, resolution = 100.0, save_all = True, append_images = labeledpdf)
        

        nonlabeledpdf = []
        for ind, i in enumerate(nonlabeledtable):
            pathway_jpg = os.path.join(PATH3 ,f"table of {getnamefromtoc(txturl, foldernomen2)} {'{0:0=2}'.format(ind+1)}_Unlabled.png")
            # i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
            i.save(pathway_jpg)
            i2 = i.convert("RGB")
            nonlabeledpdf.append(i2)
        pathway_pdf = os.path.join(PATH3 ,f"table of {getnamefromtoc(txturl, foldernomen2)}_Unlabled.pdf")
            # # i = i.resize((int(i.size[0] / 2), int(i.size[1] / 2)))
            # i2.save(pathway_pdf)
        imama = nonlabeledpdf[0]
        nonlabeledpdf.pop(0)
        imama.save(pathway_pdf, resolution = 100.0, save_all = True, append_images = nonlabeledpdf)
        
        
        #리스트 만들기
        



    
    btn_w4_test = Button(neowindow4, text = "제작중테스트", command=partial(getimgsfromfolder, r"C:\OneDrive\DDB", combox_w4_sub, ent_w4_newfilename))
    btn_w4_test.grid(row=30,column=1,columnspan=4,sticky=N+W+E+S)

    btn_w4_test2 = Button(neowindow4, text = "개별이미지", command=partial(makeindimgs, r"C:\OneDrive\DDB", combox_w4_sub, ent_w4_newfilename))
    btn_w4_test2.grid(row=31,column=1,columnspan=4,sticky=N+W+E+S)

    btn_w4_test3 = Button(neowindow4, text = "Tables", command=partial(test2, r"C:\OneDrive\DDB", combox_w4_sub, ent_w4_newfilename))
    btn_w4_test3.grid(row=32,column=1,columnspan=4,sticky=N+W+E+S)



    #구상,, 배경은 투명해야 하는가 아님 흰색이어야 하는가..
    #해결책,, 사진 만드는 함수 때로 만들고 이 함수가 투명여부 선택받아,, table 제작 시에는 흰배경, 아님 투명배경이 되도록 하는 방법이 있다.
    #구상... txt이미지 만드는애, txt 딸린 개별사진 제작기, table 제작기 ,,,사진 크기 조정하는 함수&저장함수, 는 개별생성, 


    







#1.4 메인창 레이아웃 생성
#1.4.1 스크린########################################################
scrollbar_mainscreen = Scrollbar(root)
scrollbar_mainscreen.grid(row=1,column=6,rowspan=10, sticky=N+W+E+S)
text_screen_big = Text(root, yscrollcommand=scrollbar_mainscreen.set)
text_screen_big.grid(row=1,column=1,columnspan=5,rowspan=10, sticky=N+W+E+S)
scrollbar_mainscreen.config(command=text_screen_big.yview)
#1.4.2 버튼#####################################################
driveurl_pythofolder = r"C:\OneDrive\Drug structure DB\dbmansys\drugnamedb.txt"

def showdbonmainscreen():
    label_direction.config(text="")
    text_screen_big.delete("1.0", END)
    dic_dbtxtfile = getdictfromtxt(r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt", " : ")
    for ind, i in enumerate(dic_dbtxtfile.keys()):
        text_screen_big.insert(END, f'{"{0:0=4}".format(ind + 1)}. {"{" ":30}".format(i)} {dic_dbtxtfile[i]}\n')
    label_direction.config(text="DB를 스크린에 띄웠읍니다.")

btn_showdb = Button(root, text="db보기", width=10, command=showdbonmainscreen)
btn_showdb.grid(row=0, column=1,sticky=N+W+E+S)

def sortdb():
    label_direction.config(text="")
    dic_db = getdictfromtxt(r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt", " : ")
    sorteddic = dict(sorted(dic_db.items()))
    file_opened = open(r"C:\OneDrive\DDB\DBtxtfiles\drugnamedb.txt", "w", encoding = "utf8")
    for code, name in sorteddic.items():
        file_opened.write(f"{code} : {name}\n")
    file_opened.close()
    showdbonmainscreen()
    label_direction.config(text="정렬을 완료하였읍니다.")


btn_sortdb = Button(root, text="db정렬", width=10, command=sortdb)
btn_sortdb.grid(row=0, column=2,sticky=N+W+E+S)

btn_openneowindow1 = Button(root, text="약물구조", width=20,command=openneowindow1)
btn_openneowindow1.grid(row=1, column=7,sticky=N+W+E+S)

btn_openneowindow3 = Button(root, text="한글", width=20,command=openneowindow3)
btn_openneowindow3.grid(row=2, column=7,sticky=N+W+E+S)

btn_openneowindow4 = Button(root, text="사진", width=20,command=openneowindow4)
btn_openneowindow4.grid(row=3, column=7,sticky=N+W+E+S)

# btn_openneowindow2 = Button(root, text="DB에 한글명 넣기", width=20, command=openneowindow3)
# btn_openneowindow2.grid(row=2, column=7,sticky=N+W+E+S)

# btn_openneowindow3 = Button(root, text="사진만들기", width=20, command=openneowindow4)
# btn_openneowindow3.grid(row=3, column=7,sticky=N+W+E+S)

# btn_openneowindow5 = Button(root, text="chemsketch", width=20, command=openneowindow5)
# btn_openneowindow5.grid(row=4, column=7,sticky=N+W+E+S)
#1.4.3 라벨창####################################################
label_direction = Label(root, text="라벨입니다")
label_direction.grid(row=11, column=1, columnspan=5, sticky=N+W+E+S)



#et cetera
root.mainloop()
while (True):
    pass