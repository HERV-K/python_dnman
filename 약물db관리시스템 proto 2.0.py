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
from functools import partial
#cf. 메모장
#셀레늄으로 크롤링할 때 해당 약물 창 안나오는 애는 txt 파일에 Acetaminophen : PASS 로 나타나게 하고
# 나중에 smile서 구조 그릴 때 PASS인 녀석은 빼는 걸로,,


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

    listofsubs = ["Pharmacology_katsung", "Medicinal chemistry"]
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
        

        for ind, i in enumerate(folderslist3):
            if int(str(i)) == int(str(foldernomen2)):
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
                
    btn_w1_maketxt = Button(neowindow1, text = "파일폴더 검사", command=partial(checkfileandfolders, r"C:\OneDrive\DDB", combox_w1_sub.get(), ent_w1_newfilename))
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
            file_opened.write(f"{i} :  \n")
        file_opened.close()


    btn_w1_getdrugnames = Button(neowindow1, text="입력한 약물 txt로", bg="white", fg="white", \
         command=partial(getinputnames,r"C:\OneDrive\DDB", combox_w1_sub.get(), ent_w1_newfilename))
    btn_w1_getdrugnames.grid(row=16,column=6,sticky=N+W+E+S)

    #1.3.1.6 smiles 가져오기
    def getsmiles(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        PATH1 = pathurl
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
            elif dict1[i] != " ":
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



    btn_w1_getsmile = Button(neowindow1, text="smiles",command=partial(getsmiles,r"C:\OneDrive\DDB", combox_w1_sub.get(), ent_w1_newfilename))
    btn_w1_getsmile.grid(row=16,column=7,sticky=N+W+E+S)

    #1.3.1.7 smile서 구조 얻기

    def getstrimg(pathurl, foldernomen, foldernomen2):
        #1. 경로설정
        PATH1 = pathurl
        PATH2 = PATH1 + f"\{foldernomen}"
        txturl = PATH2 + f"\{foldernomen}_tableofcontents.txt"
        foldernomen2 = int(foldernomen2.get())
        PATH3 = PATH2 + f"\{getnamefromtoc(txturl, foldernomen2)}"
        txtnametohave = f"{getnamefromtoc(txturl, foldernomen2)}.txt"
        PATHTXT = PATH3 + f"\{txtnametohave}"

        #2. 경로에 사진 폴더 생성하기
        foldernametohave = f"{getnamefromtoc(txturl, foldernomen2)}_pngs"
        checkfolderpath(PATH3, foldernametohave)
        PATH4 = PATH3 + f"\{foldernametohave}"

        #3. 구조 가져올 txt 열기
        dict1 = getdictfromtxt(PATHTXT, " : ")
        print("dict1은 ",dict1)

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

        #5. 구조 가져오기
        browser = webdriver.Chrome()
        # browser.maximize_window()
        url = "http://cdb.ics.uci.edu/cgibin/Smi2DepictWeb.py"
        browser.get(url)
        searchtab = browser.find_element(By.ID, "smiles")
        searchtab.clear()

        for i in list1:
            searchtab.send_keys(i)
            searchtab.send_keys(Keys.RETURN)

        btn = browser.find_element(By.XPATH, '//*[@id="Smi2DepictWeb"]/div[1]/div[5]/button')
        btn.click()
        time.sleep(2)
        img3 = browser.find_elements(By.CLASS_NAME, "shadow")

        for index, image in enumerate(img3):
            src = image.get_attribute("src")
            t = urlopen(src).read()
            file = open(os.path.join(PATH4, f"{list2[index]}.png"), "wb")
            file.write(t)
            print(list2[index])
        browser.close()


    btn_w1_getstrimg = Button(neowindow1, text="구조",command=partial(getstrimg,r"C:\OneDrive\DDB", combox_w1_sub.get(), ent_w1_newfilename))
    btn_w1_getstrimg.grid(row=17,column=7,sticky=N+W+E+S)


    






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