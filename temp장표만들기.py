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
root.geometry("750x500+100+50")





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



def openneowindow4():
    global neowindow4
    neowindow4 = Toplevel(root)
    neowindow4.geometry("1200x600+100+100")


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


    margintesterwideng = []
    margintesterheieng = []
    margintesterwidkor = []
    margintesterheikor = []

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
        elif combox_w4_fontcol.get() == "파":
            font_color = "RGBA(000, 051, 255, 255)"
        elif combox_w4_fontcol.get() == "노":
            font_color = "RGBA(255, 204,000, 255)"
        elif combox_w4_fontcol.get() == "초":
            font_color = "RGBA(000, 153, 000, 255)"
        else:
            font_color = "RGBA(255, 255, 255, 255)"

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
        backgroundcolor = "RGBA(0,0,0,0)"  # 글자 배경색
        fontsizetempeng = int(heightoftextimg/3)
        fontsizetempkor = int(heightoftextimg / 3)

        ##1-6. 폰트, 문장의 크기
        len_engletter = len(text1)
        len_korletter = len(text2)

        if len_engletter <= 10:
            fontsizetempeng = int(heightoftextimg/2 -10)
        elif 10< len_engletter <=15:
            fontsizetempeng = int(heightoftextimg / 3 - 7)
        elif 15 < len_engletter <= 20:
            fontsizetempeng = int(heightoftextimg / 4 - 10)
        else:
            fontsizetempeng = int(heightoftextimg / 4 - 10)

        if len_korletter <=5:
            fontsizetempkor = int(heightoftextimg/3 + 3)
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
        if combox_w4_contkor =="아니오":
            ####
            #
            #
            #

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
            pass


        """
        textimg = Image.new("RGBA", (width_img, height_img), color=backgroundcolor)
        draw = ImageDraw.Draw(textimg)

        draw.text((x_text1, y_text1), molecularname[x], font=font, fill=font_colour)
        draw.text((x_text2, y_text2), koreanna, font=font, fill=font_colour)

        makeimg(textimg, x)
        """
        #2. 사진들 덧대기
        ##2-1. 사진 크기 결정
        photo = Image.open(image)
        tempwid_img = photo.size[0]
        temphei_img = photo.size[1]

        if float(tempwid_img/temphei_img) >= float(400/250):
            #wid를 줄인다.
            img9 = photo.resize((int(widthoftextimg), int(temphei_img*widthoftextimg/tempwid_img)))
            pass
        else:
            img9 = photo.resize((int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img), int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)))
            #hei를 줄인다.
            pass

        adjustedimg = img9
        ##2-2. 사진, 텍스트 덧대기
        resultimg = Image.new("RGBA", (int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]), int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])), (0, 0, 0, 0))

        if float(tempwid_img/temphei_img) >= float(400/250):
            resultimg.paste(adjustedimg, (0, int(totalheimargin/2)))
            resultimg.paste(textedimg, (0, int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:]) * 5 / 8)))
            # resultimg.show()
        else:
            #  int((int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]) -  int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img))/2)
            resultimg.paste(adjustedimg, (int((int(combox_w4_indimgsize.get()[0:combox_w4_indimgsize.get().rfind("x")]) -  int(tempwid_img*(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x")+1:])*5/8)/temphei_img))/2), 0))
            resultimg.paste(textedimg, (0, int(int(combox_w4_indimgsize.get()[combox_w4_indimgsize.get().rfind("x") + 1:]) * 5 / 8)))
            # resultimg.show()



        ##2-3. 저장
        global w4_folder_selected
        pathway = os.path.join(w4_folder_selected, f"{text1}.png")
        resultimg.save(pathway)

        #각 콤박스별로 만들 이미지 속성 받아오는 코드 필요


    def w4_makeindimgs():
        global w4_dic_moleculename  # 한국어, 영어 이름 딕셔너리임
        global filetomakeimgs
        global w4_nomenlistofimgs
        global w4_nomenkoreae

        for ind, file in enumerate(filetomakeimgs):
            w4_makeindimgs_1(str(w4_nomenlistofimgs[ind]),str(w4_nomenkoreae[ind]), file)
        # margintesterwideng.sort()
        # margintesterwidkor.sort()
        # margintesterheieng.sort()
        # print(f"wid eng{margintesterwideng}\nwid kor{margintesterwidkor}\nhei{margintesterheieng}")
        msgbox.showinfo("무야히", "무야하")
        pass

    def w4_maketable():


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

    btn_w4_maketable = Button(neowindow4, text="장표", width=20, command=w4_maketable)
    btn_w4_maketable.grid(row=11, column=5, sticky=W + E + N + S)

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

openneowindow4()

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


btn_openneowindow3 = Button(root, text="사진만들기", width=20, command=openneowindow4)
btn_openneowindow3.grid(row=3, column=7,sticky=N+W+E+S)

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