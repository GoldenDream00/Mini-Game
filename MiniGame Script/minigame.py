#bylessy

from tkinter import *
from PIL import ImageTk, Image
import random

def endwar():
    global cash
    global wincash
    global cashtext
    global statalt1_2
    
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((110, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1600,y=946)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=430,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=600,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=770,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=940,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1110,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1280,y=157)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((100, 500))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1450,y=157)
    #############
    cash +=wincash
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((40, 110))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=340,y=870)
    #############
    cashtext = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtext.pack()
    cashtext.place(x=340, y=900)
    #############
    cashtext2 = Label(window, bg="black", fg="red", text="Money from hunting: {money}".format(money=wincash), font="Times 12") ####cash
    cashtext2.pack()
    cashtext2.place(x=357, y=970)
    #############
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((110, 40))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1600,y=914)
    #############
    refreshbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Refresh |   2" , command=refresh)
    refreshbutton.pack()
    refreshbutton.place(x=1600,y=850)
    ######
    refreshcash = Image.open("C:/Users/"+ username+ "/Desktop/minigame/redcash.png")
    refreshcash = refreshcash.resize((17, 17))
    refreshcash = ImageTk.PhotoImage(refreshcash)
    refreshcashalt = Label(window, image=refreshcash, border=False)
    refreshcashalt.image = refreshcash
    refreshcashalt.pack()
    refreshcashalt.place(x=1685,y=852)
    #############
    fightbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Fight" , command=fight)
    fightbutton.pack()
    fightbutton.place(x=1600,y=882)
    #############
    stat1_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1_2 = stat1_2.resize((100, 100))
    stat1_2 = ImageTk.PhotoImage(stat1_2)
    statalt1_2 = Label(window, image=stat1, border=False)
    statalt1_2.image = stat1_2
    statalt1_2.pack()
    statalt1_2.place(x=430,y=157)
    #############
    stat2_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat2_2 = stat2_2.resize((100, 100))
    stat2_2 = ImageTk.PhotoImage(stat2_2)
    statalt2_2 = Label(window, image=stat2_2, border=False)
    statalt2_2.image = stat2_2
    statalt2_2.pack()
    statalt2_2.place(x=600,y=157)
    #############
    stat3_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat3_2 = stat3_2.resize((100, 100))
    stat3_2 = ImageTk.PhotoImage(stat3_2)
    statalt3_2 = Label(window, image=stat3_2, border=False)
    statalt3_2.image = stat3_2
    statalt3_2.pack()
    statalt3_2.place(x=770,y=157)
    #############
    stat4_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat4_2 = stat4_2.resize((100, 100))
    stat4_2 = ImageTk.PhotoImage(stat4_2)
    statalt4_2 = Label(window, image=stat4_2, border=False)
    statalt4_2.image = stat4_2
    statalt4_2.pack()
    statalt4_2.place(x=940,y=157)
    #############
    stat5_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat5_2 = stat5_2.resize((100, 100))
    stat5_2 = ImageTk.PhotoImage(stat5_2)
    statalt5_2 = Label(window, image=stat5_2, border=False)
    statalt5_2.image = stat5_2
    statalt5_2.pack()
    statalt5_2.place(x=1110,y=157)
    #############
    stat5_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat5_2 = stat5_2.resize((100, 100))
    stat5_2 = ImageTk.PhotoImage(stat5_2)
    statalt5_2 = Label(window, image=stat5_2, border=False)
    statalt5_2.image = stat5_2
    statalt5_2.pack()
    statalt5_2.place(x=1280,y=157)
    #############
    stat7_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat7_2 = stat7_2.resize((100, 100))
    stat7_2 = ImageTk.PhotoImage(stat7_2)
    statalt7_2 = Label(window, image=stat7_2, border=False)
    statalt7_2.image = stat7_2
    statalt7_2.pack()
    statalt7_2.place(x=1450,y=157)
    #############
    #sat
    sellbutton1 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell1)
    sellbutton1.pack()
    sellbutton1.place(x=430,y=767)
    #############
    sellbutton2 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell2)
    sellbutton2.pack()
    sellbutton2.place(x=600,y=767)
    #############
    sellbutton3 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell3)
    sellbutton3.pack()
    sellbutton3.place(x=770,y=767)
    #############
    sellbutton4 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell4)
    sellbutton4.pack()
    sellbutton4.place(x=940,y=767)
    #############
    sellbutton5 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell5)
    sellbutton5.pack()
    sellbutton5.place(x=1110,y=767)
    #############
    sellbutton6 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell6)
    sellbutton6.pack()
    sellbutton6.place(x=1280,y=767)
    #############
    sellbutton7 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell7)
    sellbutton7.pack()
    sellbutton7.place(x=1450,y=767)
    nocashrefresh()

def fight():
    global fight1
    global fight2
    global fight3
    global fight4
    global fight5
    global fight6
    global fight7
    global charinstat1_x
    global charinstat2_x
    global charinstat3_x
    global charinstat4_x
    global charinstat5_x
    global charinstat6_x
    global charinstat7_x
    global charinstat1
    global charinstat2
    global charinstat3
    global charinstat4
    global charinstat5
    global charinstat6
    global charinstat7
    global chardmgs
    global sellbutton1
    global sellbutton2
    global sellbutton3
    global sellbutton4
    global sellbutton5
    global sellbutton6
    global sellbutton7
    global fightbutton
    global wincash
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((110, 40))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1600,y=842)
    nextroundbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Next Round" , command=nocashrefresh)
    nextroundbutton.pack()
    nextroundbutton.place(x=1600,y=914)
    endwarbutton = Button(window, width=14, bg="red", fg="white", border=False , text="End The War" , command=endwar)
    endwarbutton.pack()
    endwarbutton.place(x=1600,y=946)
    if len(charinstat1) == 1:
        black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
        black = black.resize((110, 30))
        black = ImageTk.PhotoImage(black)
        blackalt1 = Label(window, image=black, border=False)
        blackalt1.image = black
        blackalt1.pack()
        blackalt1.place(x=1600,y=882)
        sellbutton1.destroy()
        fight1 = True
        charinstat1_x.append(randomchar1_x)
        enemyr1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1_x+".png")
        enemyr1 = enemyr1.resize((100, 100))
        enemyr1 = ImageTk.PhotoImage(enemyr1)
        enemyr1panel = Label(window, image=enemyr1, border=False)
        enemyr1panel.image = enemyr1
        enemyr1panel.pack()
        enemyr1panel.place(x=430,y=157)
        for item in charinstat1_x:
            chardmgs1_x = chardmgs[item]
        for item in charinstat1:
            chardmgs1 = chardmgs[item]
        chardmgs1_x = int(chardmgs1_x)
        chardmgs1 = int(chardmgs1)
        if chardmgs1 > chardmgs1_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=465,y=617)
        elif chardmgs1 < chardmgs1_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=465,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=465,y=437)
    
    if len(charinstat2) == 1 and fight1 == True:
        black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
        black = black.resize((110, 30))
        black = ImageTk.PhotoImage(black)
        blackalt1 = Label(window, image=black, border=False)
        blackalt1.image = black
        blackalt1.pack()
        blackalt1.place(x=1600,y=882)
        sellbutton2.destroy()
        fight2 = True
        charinstat2_x.append(randomchar2_x)
        enemyr2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2_x+".png")
        enemyr2 = enemyr2.resize((100, 100))
        enemyr2 = ImageTk.PhotoImage(enemyr2)
        enemyr2panel = Label(window, image=enemyr2, border=False)
        enemyr2panel.image = enemyr2
        enemyr2panel.pack()
        enemyr2panel.place(x=600,y=157)
        for item in charinstat2_x:
            chardmgs2_x = chardmgs[item]
        for item in charinstat2:
            chardmgs2 = chardmgs[item]
        chardmgs2_x = int(chardmgs2_x)
        chardmgs2 = int(chardmgs2)
        if chardmgs2 > chardmgs2_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=635,y=617)
        elif chardmgs2 < chardmgs2_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=635,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=635,y=437)

    if len(charinstat3) == 1 and fight2 == True:
        black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
        black = black.resize((110, 30))
        black = ImageTk.PhotoImage(black)
        blackalt1 = Label(window, image=black, border=False)
        blackalt1.image = black
        blackalt1.pack()
        blackalt1.place(x=1600,y=882)
        sellbutton3.destroy()
        fight3 = True
        charinstat3_x.append(randomchar3_x)
        enemyr3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3_x+".png")
        enemyr3 = enemyr3.resize((100, 100))
        enemyr3 = ImageTk.PhotoImage(enemyr3)
        enemyr3panel = Label(window, image=enemyr3, border=False)
        enemyr3panel.image = enemyr3
        enemyr3panel.pack()
        enemyr3panel.place(x=770,y=157)
        for item in charinstat3_x:
            chardmgs3_x = chardmgs[item]
        for item in charinstat3:
            chardmgs3 = chardmgs[item]
        chardmgs3_x = int(chardmgs3_x)
        chardmgs3 = int(chardmgs3)
        if chardmgs3 > chardmgs3_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=805,y=617)
        elif chardmgs3 < chardmgs3_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=805,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=805,y=437)
    
    if len(charinstat4) == 1 and fight3 == True:
        sellbutton4.destroy()
        fight4 = True
        charinstat4_x.append(randomchar4_x)
        enemyr4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4_x+".png")
        enemyr4 = enemyr4.resize((100, 100))
        enemyr4 = ImageTk.PhotoImage(enemyr4)
        enemyr4panel = Label(window, image=enemyr4, border=False)
        enemyr4panel.image = enemyr4
        enemyr4panel.pack()
        enemyr4panel.place(x=940,y=157)
        for item in charinstat4_x:
            chardmgs4_x = chardmgs[item]
        for item in charinstat4:
            chardmgs4 = chardmgs[item]
        chardmgs4_x = int(chardmgs4_x)
        chardmgs4 = int(chardmgs4)
        if chardmgs4 > chardmgs4_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=972,y=617)
        elif chardmgs4 < chardmgs4_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=972,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=972,y=437)
    
    if len(charinstat5) == 1 and fight4 == True:
        sellbutton5.destroy()
        fight5 = True
        charinstat5_x.append(randomchar5_x)
        enemyr5 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar5_x+".png")
        enemyr5 = enemyr5.resize((100, 100))
        enemyr5 = ImageTk.PhotoImage(enemyr5)
        enemyr5panel = Label(window, image=enemyr5, border=False)
        enemyr5panel.image = enemyr5
        enemyr5panel.pack()
        enemyr5panel.place(x=1110,y=157)
        for item in charinstat5_x:
            chardmgs5_x = chardmgs[item]
        for item in charinstat5:
            chardmgs5 = chardmgs[item]
        chardmgs5_x = int(chardmgs5_x)
        chardmgs5 = int(chardmgs5)
        if chardmgs5 > chardmgs5_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1145,y=617)
        elif chardmgs5 < chardmgs5_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1145,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=1145,y=437)

    if len(charinstat6) == 1 and fight5 == True:
        sellbutton6.destroy()
        fight6 = True
        charinstat6_x.append(randomchar6_x)
        enemyr6 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar6_x+".png")
        enemyr6 = enemyr6.resize((100, 100))
        enemyr6 = ImageTk.PhotoImage(enemyr6)
        enemyr6panel = Label(window, image=enemyr6, border=False)
        enemyr6panel.image = enemyr6
        enemyr6panel.pack()
        enemyr6panel.place(x=1280,y=157)
        for item in charinstat6_x:
            chardmgs6_x = chardmgs[item]
        for item in charinstat6:
            chardmgs6 = chardmgs[item]
        chardmgs6_x = int(chardmgs6_x)
        chardmgs6 = int(chardmgs6)
        if chardmgs6 > chardmgs6_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1315,y=617)
        elif chardmgs6 < chardmgs6_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1315,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=1315,y=437)

    if len(charinstat7) == 1 and fight6 == True:
        sellbutton7.destroy()
        fight7 = True
        charinstat7_x.append(randomchar7_x)
        enemyr7 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar7_x+".png")
        enemyr7 = enemyr7.resize((100, 100))
        enemyr7 = ImageTk.PhotoImage(enemyr7)
        enemyr7panel = Label(window, image=enemyr7, border=False)
        enemyr7panel.image = enemyr7
        enemyr7panel.pack()
        enemyr7panel.place(x=1450,y=157)
        for item in charinstat7_x:
            chardmgs7_x = chardmgs[item]
        for item in charinstat7:
            chardmgs7 = chardmgs[item]
        chardmgs7_x = int(chardmgs7_x)
        chardmgs7 = int(chardmgs7)
        if chardmgs7 > chardmgs7_x:
            vsresults.append("main")
            wincash +=1
            winner = Label(window, bg="black" , fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1485,y=617)
        elif chardmgs7 < chardmgs7_x:
            vsresults.append("enemy")
            winner = Label(window, bg="black", fg="cyan" , text="WON!")
            winner.pack()
            winner.place(x=1485,y=277)
        else:
            draw = Label(window, bg="black", fg="cyan" , text="DRAW!")
            draw.pack()
            draw.place(x=1485,y=437)
        nextroundbutton.destroy()

    else:
        pass



def update():
    global charinstat1
    global charinstatall
    global charstats
    global cash

    try:
        pass
        #if charinstatall.count("Sorcerer") == 0:
        #    black = Image.open("C:/Users/"+ username+ "/Desktop/tftmaybe/beyaz.png")
        #    black = black.resize((130, 50))
        #    black = ImageTk.PhotoImage(black)
        #    blackalt1 = Label(window, image=black, border=False)
        #    blackalt1.image = black
        #    blackalt1.pack()
        #    blackalt1.place(x=35,y=230)
        #else:
        #    (charinstatall.count("Sorcerer") >= 1)
        #    stats1 = Label(window, bg="black", fg="red", text="Sorcerer {Sorcerer} / 9".format(Sorcerer=charinstatall.count("Sorcerer")), font="Times 16")
        #    stats1.pack()
        #    stats1.place(x=35, y=250)
    except:
        pass
        
    try:
        pass
        #if charinstatall.count("Assasin") == 0:
        #    black = Image.open("C:/Users/"+ username+ "/Desktop/tftmaybe/beyaz.png")
        #    black = black.resize((130, 50))
        #    black = ImageTk.PhotoImage(black)
        #    blackalt1 = Label(window, image=black, border=False)
        #    blackalt1.image = black
        #    blackalt1.pack()
        #    blackalt1.place(x=35,y=280)
        #else:
        #    (charinstatall.count("Assasin") >= 1)
        #    stats2 = Label(window, bg="black", fg="red", text="Assasin {assasin} / 9".format(assasin=charinstatall.count("Assasin")), font="Times 16")
        #    stats2.pack()
        #    stats2.place(x=35, y=280)
    except:
        pass
#############
def sell1():
    global sellbutton1
    global charinstat1
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=430,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=430,y=657)
    charinstat1str = str(charinstat1[0])
    charinstatall.remove(charstats[charinstat1str])
    for item in charinstat1:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat1:
        chardmgs1 = chardmgs[item]
    chardmgs1 = int(chardmgs1)
    charalldmgs -= chardmgs1
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat1 = []
    update()
#############
def sell2():
    global sellbutton2
    global charinstat2
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=600,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=600,y=657)
    charinstat2str = str(charinstat2[0])
    charinstatall.remove(charstats[charinstat2str])
    for item in charinstat2:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat2:
        chardmgs2 = chardmgs[item]
    chardmgs2 = int(chardmgs2)
    charalldmgs -= chardmgs2
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740) 
    charinstat2 = []
    update()
#############
def sell3():
    global sellbutton3
    global charinstat3
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=770,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=770,y=657)
    charinstat3str = str(charinstat3[0])
    charinstatall.remove(charstats[charinstat3str])
    for item in charinstat3:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat3:
        chardmgs3 = chardmgs[item]
    chardmgs3 = int(chardmgs3)
    charalldmgs -= chardmgs3
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat3 = []
    update()
#############
def sell4():
    global sellbutton4
    global charinstat4
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=940,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=940,y=657)
    charinstat4str = str(charinstat4[0])
    charinstatall.remove(charstats[charinstat4str])
    for item in charinstat4:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat4:
        chardmgs4 = chardmgs[item]
    chardmgs4 = int(chardmgs4)
    charalldmgs -= chardmgs4
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat4 = []
    update()
#############
def sell5():
    global sellbutton5
    global charinstat5
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1110,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=1110,y=657)
    charinstat5str = str(charinstat5[0])
    charinstatall.remove(charstats[charinstat5str])
    for item in charinstat5:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat5:
        chardmgs5 = chardmgs[item]
    chardmgs5 = int(chardmgs5)
    charalldmgs -= chardmgs5
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat5 = []
    update()
#############
def sell6():
    global sellbutton6
    global charinstat6
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1280,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=1280,y=657)
    charinstat6str = str(charinstat6[0])
    charinstatall.remove(charstats[charinstat6str])
    for item in charinstat6:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat6:
        chardmgs6 = chardmgs[item]
    chardmgs6 = int(chardmgs6)
    charalldmgs -= chardmgs6
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat6 = []
    update()
#############
def sell7():
    global sellbutton7
    global charinstat7
    global charinstatall
    global charstats
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((130, 100))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1450,y=657)
    stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
    stat1 = stat1.resize((100, 100))
    stat1 = ImageTk.PhotoImage(stat1)
    statalt1 = Label(window, image=stat1, border=False)
    statalt1.image = stat1
    statalt1.pack()
    statalt1.place(x=1450,y=657)
    charinstat7str = str(charinstat7[0])
    charinstatall.remove(charstats[charinstat7str])
    for item in charinstat7:
        sellcash = charcashs[item]
    sellcash = int(sellcash)
    cash = cash + sellcash
    cashtext.destroy()
    cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
    cashtextt.pack()
    cashtextt.place(x=340, y=900)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((50, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=110,y=740)
    for item in charinstat7:
        chardmgs7 = chardmgs[item]
    chardmgs7 = int(chardmgs7)
    charalldmgs -= chardmgs7
    stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
    stats1.pack()
    stats1.place(x=110, y=740)
    charinstat7 = []
    update()
#############


def buy1():
    global charinstat1
    global charinstatall
    global charstats
    global panelalt1
    global randomchar1
    global charinstat1
    global buy1button
    global cashprice1
    global cashalt1
    global cashtext
    global cash
    global charcashs
    global charalldmgs

    charcashsint = int(charcashs[randomchar1])
    if (len(charinstat1) == 1) and (len(charinstat2) == 1) and (len(charinstat3) == 1) and (len(charinstat4) == 1) and (len(charinstat5) == 1) and (len(charinstat6) == 1) and (len(charinstat7) == 1) or (charcashsint > cash):
        pass
    else:
        cashprice1.destroy()
        cashalt1.destroy()
        panelalt1.destroy()
        buy1button.destroy()
        char1_1.destroy()
        cashtext.destroy()
        cash = cash - charcashsint
        cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
        cashtextt.pack()
        cashtextt.place(x=340, y=900)
        if len(charinstat1) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat1.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=430,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat1:
                chardmgs1 = chardmgs[item]
            chardmgs1 = int(chardmgs1)
            charalldmgs += chardmgs1
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)       
        elif len(charinstat2) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat2.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=600,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat2:
                chardmgs2 = chardmgs[item]
            chardmgs2 = int(chardmgs2)
            charalldmgs += chardmgs2
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740) 
        elif len(charinstat3) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat3.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=770,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=100,y=450)
            for item in charinstat3:
                chardmgs3 = chardmgs[item]
            chardmgs3 = int(chardmgs3)
            charalldmgs += chardmgs3
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat4) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat4.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=940,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat4:
                chardmgs4 = chardmgs[item]
            chardmgs4 = int(chardmgs4)
            charalldmgs += chardmgs4
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat5) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat5.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1110,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110, y=740)
            for item in charinstat5:
                chardmgs5 = chardmgs[item]
            chardmgs5 = int(chardmgs5)
            charalldmgs += chardmgs5
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110,y=740)
        elif len(charinstat6) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat6.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1280,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat6:
                chardmgs6 = chardmgs[item]
            chardmgs6 = int(chardmgs6)
            charalldmgs += chardmgs6
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat7) == 0:
            charinstatall.append(charstats[randomchar1])
            charinstat7.append(randomchar1)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1450,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat7:
                chardmgs7 = chardmgs[item]
            chardmgs7 = int(chardmgs7)
            charalldmgs += chardmgs7
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        else:
            pass
#############
def buy2():
    global panelalt2
    global randomchar2
    global buy2button
    global cashprice2
    global cashalt2
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    
    charcashsint = int(charcashs[randomchar2])
    if (len(charinstat1) == 1) and (len(charinstat2) == 1) and (len(charinstat3) == 1) and (len(charinstat4) == 1) and (len(charinstat5) == 1) and (len(charinstat6) == 1) and (len(charinstat7) == 1) or (charcashsint > cash):
        pass
    else:
        cashprice2.destroy()
        cashalt2.destroy()
        panelalt2.destroy()
        buy2button.destroy()
        char2_1.destroy()
        cashtext.destroy()
        cash = cash - charcashsint
        cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
        cashtextt.pack()
        cashtextt.place(x=340, y=900)
        if len(charinstat1) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat1.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=430,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat1:
                chardmgs1 = chardmgs[item]
            chardmgs1 = int(chardmgs1)
            charalldmgs += chardmgs1
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat2) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat2.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=600,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat2:
                chardmgs2 = chardmgs[item]
            chardmgs2 = int(chardmgs2)
            charalldmgs += chardmgs2
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740) 
        elif len(charinstat3) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat3.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=770,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat3:
                chardmgs3 = chardmgs[item]
            chardmgs3 = int(chardmgs3)
            charalldmgs += chardmgs3
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110,y=740)
        elif len(charinstat4) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat4.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=940,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat4:
                chardmgs4 = chardmgs[item]
            chardmgs4 = int(chardmgs4)
            charalldmgs += chardmgs4
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat5) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat5.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1110,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat5:
                chardmgs5 = chardmgs[item]
            chardmgs5 = int(chardmgs5)
            charalldmgs += chardmgs5
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat6) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat6.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1280,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat6:
                chardmgs6 = chardmgs[item]
            chardmgs6 = int(chardmgs6)
            charalldmgs += chardmgs6
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat7) == 0:
            charinstatall.append(charstats[randomchar2])
            charinstat7.append(randomchar2)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1450,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat7:
                chardmgs7 = chardmgs[item]
            chardmgs7 = int(chardmgs7)
            charalldmgs += chardmgs7
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        else:
            pass
#############
def buy3():
    global panelalt3
    global randomchar3
    global buy3button
    global cashprice3
    global cashalt3
    global cashtext
    global cash
    global charcashs
    global charalldmgs
    
    charcashsint = int(charcashs[randomchar3])
    if (len(charinstat1) == 1) and (len(charinstat2) == 1) and (len(charinstat3) == 1) and (len(charinstat4) == 1) and (len(charinstat5) == 1) and (len(charinstat6) == 1) and (len(charinstat7) == 1) or (charcashsint > cash):
        pass
    else:
        cashprice3.destroy()
        cashalt3.destroy()
        panelalt3.destroy()
        buy3button.destroy()
        char3_1.destroy()
        cashtext.destroy()
        cash = cash - charcashsint
        cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
        cashtextt.pack()
        cashtextt.place(x=340, y=900)
        if len(charinstat1) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat1.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=430,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat1:
                chardmgs1 = chardmgs[item]
            chardmgs1 = int(chardmgs1)
            charalldmgs += chardmgs1
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat2) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat2.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=600,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat2:
                chardmgs2 = chardmgs[item]
            chardmgs2 = int(chardmgs2)
            charalldmgs += chardmgs2
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)    
        elif len(charinstat3) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat3.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=770,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat3:
                chardmgs3 = chardmgs[item]
            chardmgs3 = int(chardmgs3)
            charalldmgs += chardmgs3
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat4) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat4.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=940,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat4:
                chardmgs4 = chardmgs[item]
            chardmgs4 = int(chardmgs4)
            charalldmgs += chardmgs4
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat5) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat5.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1110,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat5:
                chardmgs5 = chardmgs[item]
            chardmgs5 = int(chardmgs5)
            charalldmgs += chardmgs5
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat6) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat6.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1280,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat6:
                chardmgs6 = chardmgs[item]
            chardmgs6 = int(chardmgs6)
            charalldmgs += chardmgs6
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat7) == 0:
            charinstatall.append(charstats[randomchar3])
            charinstat7.append(randomchar3)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1450,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat7:
                chardmgs7 = chardmgs[item]
            chardmgs7 = int(chardmgs7)
            charalldmgs += chardmgs7
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)

        else:
            pass
#############
def buy4():
    global panelalt4
    global randomchar4
    global buy4button
    global cashprice4
    global cashalt4
    global cashtext
    global cash
    global charcashs
    global charalldmgs


    charcashsint = int(charcashs[randomchar4])
    if (len(charinstat1) == 1) and (len(charinstat2) == 1) and (len(charinstat3) == 1) and (len(charinstat4) == 1) and (len(charinstat5) == 1) and (len(charinstat6) == 1) and (len(charinstat7) == 1) or (charcashsint > cash):
        pass
    else:
        cashprice4.destroy()
        cashalt4.destroy()
        panelalt4.destroy()
        buy4button.destroy()
        char4_1.destroy()
        cashtext.destroy()
        cash = cash - charcashsint
        cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
        cashtextt.pack()
        cashtextt.place(x=340, y=900)
        if len(charinstat1) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat1.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=430,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat1:
                chardmgs1 = chardmgs[item]
            chardmgs1 = int(chardmgs1)
            charalldmgs += chardmgs1
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat2) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat2.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=600,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat2:
                chardmgs2 = chardmgs[item]
            chardmgs2 = int(chardmgs2)
            charalldmgs += chardmgs2
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740) 
        elif len(charinstat3) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat3.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=770,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat3:
                chardmgs3 = chardmgs[item]
            chardmgs3 = int(chardmgs3)
            charalldmgs += chardmgs3
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat4) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat4.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=940,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat4:
                chardmgs4 = chardmgs[item]
            chardmgs4 = int(chardmgs4)
            charalldmgs += chardmgs4
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat5) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat5.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1110,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat5:
                chardmgs5 = chardmgs[item]
            chardmgs5 = int(chardmgs5)
            charalldmgs += chardmgs5
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat6) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat6.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1280,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat6:
                chardmgs6 = chardmgs[item]
            chardmgs6 = int(chardmgs6)
            charalldmgs += chardmgs6
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        elif len(charinstat7) == 0:
            charinstatall.append(charstats[randomchar4])
            charinstat7.append(randomchar4)
            imgs = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
            imgs = imgs.resize((105, 100))
            imgs = ImageTk.PhotoImage(imgs)
            panelalts = Label(window, image=imgs, border=False)
            panelalts.image = imgs
            panelalts.pack()
            panelalts.place(x=1450,y=657)
            update()
            black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
            black = black.resize((50, 30))
            black = ImageTk.PhotoImage(black)
            blackalt1 = Label(window, image=black, border=False)
            blackalt1.image = black
            blackalt1.pack()
            blackalt1.place(x=110,y=740)
            for item in charinstat7:
                chardmgs7 = chardmgs[item]
            chardmgs7 = int(chardmgs7)
            charalldmgs += chardmgs7
            stats1 = Label(window, bg="black", fg="red", text=charalldmgs, font="Times 16")
            stats1.pack()
            stats1.place(x=110, y=740)
        else:
            pass
#############
def refresh():
    global randomchar1
    global randomchar2
    global randomchar3
    global randomchar4
    global panelalt1
    global panelalt2
    global panelalt3
    global panelalt4
    global char1_1
    global char2_1
    global char3_1
    global char4_1    
    global buy1button
    global buy2button
    global buy3button
    global buy4button
    global cashprice1
    global cashprice2
    global cashprice3
    global cashprice4
    global cashalt1
    global cashalt2
    global cashalt3
    global cashalt4
    global cash
    if cash >= 2:
        cashtext.destroy()
        panelalt1.destroy()
        panelalt2.destroy()
        panelalt3.destroy()
        panelalt4.destroy()
        cashprice1.destroy()
        cashprice2.destroy()
        cashprice3.destroy()
        cashprice4.destroy()
        cashalt1.destroy()
        cashalt2.destroy()
        cashalt3.destroy()
        cashalt4.destroy()
        char1_1.destroy()
        char2_1.destroy()
        char3_1.destroy()
        char4_1.destroy()
        panelalt1.destroy()
        panelalt2.destroy()
        panelalt3.destroy()
        panelalt4.destroy()
        buy1button.destroy()
        buy2button.destroy()
        buy3button.destroy()
        buy4button.destroy()
        cash = cash - 2
        cashtextt = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
        cashtextt.pack()
        cashtextt.place(x=340, y=900)
        buy1button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy1)
        buy1button.pack()
        buy1button.place(x=628, y=990)
        buy2button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy2)
        buy2button.pack()
        buy2button.place(x=848, y=990)
        buy3button = Button(window, width=14 , bg="red", fg="white", border=False , text="Buy" , command=buy3)
        buy3button.pack()
        buy3button.place(x=1068, y=990)
        buy4button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy4)
        buy4button.pack()
        buy4button.place(x=1288, y=990)
        randomchar1 = random.choice(chars)
        randomchar2 = random.choice(chars)
        randomchar3 = random.choice(chars)
        randomchar4 = random.choice(chars)
        char1_1 = Label(window, bg="black", fg="red", text=charstats[randomchar1], font="Times 12") ####suikastçı büyücü text
        char1_1.pack()
        char1_1.place(x=650, y=945)
        cash1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
        cash1 = cash1.resize((30, 15))
        cash1 = ImageTk.PhotoImage(cash1)
        cashalt1 = Label(window, image=cash1, border=False)
        cashalt1.image = cash1
        cashalt1.pack()
        cashalt1.place(x=675,y=970)
        cashprice1 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar1], font="Times 13") ####cash
        cashprice1.pack()
        cashprice1.place(x=663, y=965)
        imgalt1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
        imgalt1 = imgalt1.resize((100, 100))
        imgalt1 = ImageTk.PhotoImage(imgalt1)
        panelalt1 = Label(window, image=imgalt1, border=False)
        panelalt1.image = imgalt1
        panelalt1.pack()
        panelalt1.place(x=630,y=847)

        ######

        char2_1 = Label(window, bg="black", fg="red", text=charstats[randomchar2], font="Times 12") ####suikastçı büyücü text
        char2_1.pack()
        char2_1.place(x=870, y=945)
        cash2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
        cash2 = cash2.resize((30, 15))
        cash2 = ImageTk.PhotoImage(cash2)
        cashalt2 = Label(window, image=cash2, border=False)
        cashalt2.image = cash2
        cashalt2.pack()
        cashalt2.place(x=895,y=970)
        cashprice2 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar2], font="Times 13") ####cash
        cashprice2.pack()
        cashprice2.place(x=883, y=965)
        imgalt2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
        imgalt2 = imgalt2.resize((100, 100))
        imgalt2 = ImageTk.PhotoImage(imgalt2)
        panelalt2 = Label(window, image=imgalt2, border=False)
        panelalt2.image = imgalt2
        panelalt2.pack()
        panelalt2.place(x=850,y=847)

        ######

        char3_1 = Label(window, bg="black", fg="red", text=charstats[randomchar3], font="Times 12") ####suikastçı büyücü text
        char3_1.pack()
        char3_1.place(x=1090, y=945)
        cash3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
        cash3 = cash3.resize((30, 15))
        cash3 = ImageTk.PhotoImage(cash3)
        cashalt3 = Label(window, image=cash3, border=False)
        cashalt3.image = cash3
        cashalt3.pack()
        cashalt3.place(x=1112,y=970)
        cashprice3 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar3], font="Times 13") ####cash
        cashprice3.pack()
        cashprice3.place(x=1100, y=965)
        imgalt3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
        imgalt3 = imgalt3.resize((100, 100))
        imgalt3 = ImageTk.PhotoImage(imgalt3)
        panelalt3 = Label(window, image=imgalt3, border=False)
        panelalt3.image = imgalt3
        panelalt3.pack()
        panelalt3.place(x=1070,y=847)

        #####

        char4_1 = Label(window, bg="black", fg="red", text=charstats[randomchar4], font="Times 12") ####suikastçı büyücü text
        char4_1.pack()
        char4_1.place(x=1312, y=945)
        cash4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
        cash4 = cash4.resize((30, 15))
        cash4 = ImageTk.PhotoImage(cash4)
        cashalt4 = Label(window, image=cash4, border=False)
        cashalt4.image = cash4
        cashalt4.pack()
        cashalt4.place(x=1334,y=970)
        cashprice4 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar4], font="Times 13") ####cash
        cashprice4.pack()
        cashprice4.place(x=1322, y=965)
        imgalt4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
        imgalt4 = imgalt4.resize((100, 100))
        imgalt4 = ImageTk.PhotoImage(imgalt4)
        panelalt4 = Label(window, image=imgalt4, border=False)
        panelalt4.image = imgalt4
        panelalt4.pack()
        panelalt4.place(x=1290,y=847)
    else:
        pass
#############
def nocashrefresh():
    global randomchar1
    global randomchar2
    global randomchar3
    global randomchar4
    global panelalt1
    global panelalt2
    global panelalt3
    global panelalt4
    global char1_1
    global char2_1
    global char3_1
    global char4_1    
    global buy1button
    global buy2button
    global buy3button
    global buy4button
    global cashprice1
    global cashprice2
    global cashprice3
    global cashprice4
    global cashalt1
    global cashalt2
    global cashalt3
    global cashalt4
    global cash
    global wincash
    panelalt1.destroy()
    panelalt2.destroy()
    panelalt3.destroy()
    panelalt4.destroy()
    cashprice1.destroy()
    cashprice2.destroy()
    cashprice3.destroy()
    cashprice4.destroy()
    cashalt1.destroy()
    cashalt2.destroy()
    cashalt3.destroy()
    cashalt4.destroy()
    char1_1.destroy()
    char2_1.destroy()
    char3_1.destroy()
    char4_1.destroy()
    panelalt1.destroy()
    panelalt2.destroy()
    panelalt3.destroy()
    panelalt4.destroy()
    buy1button.destroy()
    buy2button.destroy()
    buy3button.destroy()
    buy4button.destroy()
    refreshbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Refresh |   2" , command=refresh)
    refreshbutton.pack()
    refreshbutton.place(x=1600,y=850)
    #############
    refreshcash = Image.open("C:/Users/"+ username+ "/Desktop/minigame/redcash.png")
    refreshcash = refreshcash.resize((17, 17))
    refreshcash = ImageTk.PhotoImage(refreshcash)
    refreshcashalt = Label(window, image=refreshcash, border=False)
    refreshcashalt.image = refreshcash
    refreshcashalt.pack()
    refreshcashalt.place(x=1685,y=852)
    fightbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Fight" , command=fight)
    fightbutton.pack()
    fightbutton.place(x=1600,y=882)
    buy1button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy1)
    buy1button.pack()
    buy1button.place(x=628, y=990)
    buy2button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy2)
    buy2button.pack()
    buy2button.place(x=848, y=990)
    buy3button = Button(window, width=14 , bg="red", fg="white", border=False , text="Buy" , command=buy3)
    buy3button.pack()
    buy3button.place(x=1068, y=990)
    buy4button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy4)
    buy4button.pack()
    buy4button.place(x=1288, y=990)
    randomchar1 = random.choice(chars)
    randomchar2 = random.choice(chars)
    randomchar3 = random.choice(chars)
    randomchar4 = random.choice(chars)
    char1_1 = Label(window, bg="black", fg="red", text=charstats[randomchar1], font="Times 12") ####suikastçı büyücü text
    char1_1.pack()
    char1_1.place(x=650, y=945)
    cash1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
    cash1 = cash1.resize((30, 15))
    cash1 = ImageTk.PhotoImage(cash1)
    cashalt1 = Label(window, image=cash1, border=False)
    cashalt1.image = cash1
    cashalt1.pack()
    cashalt1.place(x=675,y=970)
    cashprice1 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar1], font="Times 13") ####cash
    cashprice1.pack()
    cashprice1.place(x=663, y=965)
    imgalt1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
    imgalt1 = imgalt1.resize((100, 100))
    imgalt1 = ImageTk.PhotoImage(imgalt1)
    panelalt1 = Label(window, image=imgalt1, border=False)
    panelalt1.image = imgalt1
    panelalt1.pack()
    panelalt1.place(x=630,y=847)
#############
    char2_1 = Label(window, bg="black", fg="red", text=charstats[randomchar2], font="Times 12") ####suikastçı büyücü text
    char2_1.pack()
    char2_1.place(x=870, y=945)
    cash2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
    cash2 = cash2.resize((30, 15))
    cash2 = ImageTk.PhotoImage(cash2)
    cashalt2 = Label(window, image=cash2, border=False)
    cashalt2.image = cash2
    cashalt2.pack()
    cashalt2.place(x=895,y=970)
    cashprice2 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar2], font="Times 13") ####cash
    cashprice2.pack()
    cashprice2.place(x=883, y=965)
    imgalt2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
    imgalt2 = imgalt2.resize((100, 100))
    imgalt2 = ImageTk.PhotoImage(imgalt2)
    panelalt2 = Label(window, image=imgalt2, border=False)
    panelalt2.image = imgalt2
    panelalt2.pack()
    panelalt2.place(x=850,y=847)
#############
    char3_1 = Label(window, bg="black", fg="red", text=charstats[randomchar3], font="Times 12") ####suikastçı büyücü text
    char3_1.pack()
    char3_1.place(x=1090, y=945)
    cash3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
    cash3 = cash3.resize((30, 15))
    cash3 = ImageTk.PhotoImage(cash3)
    cashalt3 = Label(window, image=cash3, border=False)
    cashalt3.image = cash3
    cashalt3.pack()
    cashalt3.place(x=1112,y=970)
    cashprice3 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar3], font="Times 13") ####cash
    cashprice3.pack()
    cashprice3.place(x=1100, y=965)
    imgalt3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
    imgalt3 = imgalt3.resize((100, 100))
    imgalt3 = ImageTk.PhotoImage(imgalt3)
    panelalt3 = Label(window, image=imgalt3, border=False)
    panelalt3.image = imgalt3
    panelalt3.pack()
    panelalt3.place(x=1070,y=847)
#############
    char4_1 = Label(window, bg="black", fg="red", text=charstats[randomchar4], font="Times 12") ####suikastçı büyücü text
    char4_1.pack()
    char4_1.place(x=1312, y=945)
    cash4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
    cash4 = cash4.resize((30, 15))
    cash4 = ImageTk.PhotoImage(cash4)
    cashalt4 = Label(window, image=cash4, border=False)
    cashalt4.image = cash4
    cashalt4.pack()
    cashalt4.place(x=1334,y=970)
    cashprice4 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar4], font="Times 13") ####cash
    cashprice4.pack()
    cashprice4.place(x=1322, y=965)
    imgalt4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
    imgalt4 = imgalt4.resize((100, 100))
    imgalt4 = ImageTk.PhotoImage(imgalt4)
    panelalt4 = Label(window, image=imgalt4, border=False)
    panelalt4.image = imgalt4
    panelalt4.pack()
    panelalt4.place(x=1290,y=847)
    black = Image.open("C:/Users/"+ username+ "/Desktop/minigame/black.png")
    black = black.resize((110, 30))
    black = ImageTk.PhotoImage(black)
    blackalt1 = Label(window, image=black, border=False)
    blackalt1.image = black
    blackalt1.pack()
    blackalt1.place(x=1600,y=914)
    wincash = 0



#inside
cash = 30
wincash = 0
charinstat1 = []
charinstat2 = []
charinstat3 = []
charinstat4 = []
charinstat5 = []
charinstat6 = []
charinstat7 = []
charinstatall = []
charinstat1_x = []
charinstat2_x = []
charinstat3_x = []
charinstat4_x = []
charinstat5_x = []
charinstat6_x = []
charinstat7_x = []
charinstatall_x = []
fight1 = False
fight2 = False
fight3 = False
fight4 = False
fight5 = False
fight6 = False
fight7 = False
vsresults = []
chars = ["Ahri" , "Zed" , "Annie" , "Veigar"]
charstats = {"Ahri":"Sorcerer" , "Zed":"Assasin" , "Annie":"Sorcerer" , "Veigar":"Sorcerer"}
charcashs = {"Ahri":"2" , "Zed":"3", "Annie":"1", "Veigar":"2"}
chardmgs = {"Ahri":"700", "Zed":"1100", "Annie":"600", "Veigar":"900"}
charalldmgs = 0


randomchar1_x = random.choice(chars)
randomchar2_x = random.choice(chars)
randomchar3_x = random.choice(chars)
randomchar4_x = random.choice(chars)
randomchar5_x = random.choice(chars)
randomchar6_x = random.choice(chars)
randomchar7_x = random.choice(chars)
randomchar1 = random.choice(chars)
randomchar2 = random.choice(chars)
randomchar3 = random.choice(chars)
randomchar4 = random.choice(chars)

username = input("What is your computer USER'name? ")

window = Tk()
window.title("Minigame")
window.state("zoomed")
window.configure(background="black")
Label2 = Label(window, bg="black", fg="red", text="by Lessy", font="Times 8")
Label2.pack()
Label2.place(x=1870, y=5)
####################################################


#sides
leftside = Image.open("C:/Users/"+ username+ "/Desktop/minigame/leftside.png")
leftside = leftside.resize((130, 700))
leftside = ImageTk.PhotoImage(leftside)
leftsidepanel = Label(window, image=leftside, border=False)
leftsidepanel.image = leftside
leftsidepanel.pack()
leftsidepanel.place(x=7,y=140)
#############
bottom = Image.open("C:/Users/"+ username+ "/Desktop/minigame/bottom.png")
bottom = bottom.resize((1030, 200))
bottom = ImageTk.PhotoImage(bottom)
bottompanel = Label(window, image=bottom, border=False)
bottompanel.image = bottom
bottompanel.pack()
bottompanel.place(x=500,y=800)
####################################################

#cash
cashbigpic = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
cashbigpic = cashbigpic.resize((150, 100))
cashbigpic = ImageTk.PhotoImage(cashbigpic)
cashbigpicpanel = Label(window, image=cashbigpic, border=False)
cashbigpicpanel.image = cashbigpic
cashbigpicpanel.pack()
cashbigpicpanel.place(x=350,y=870)
##############
cashtext = Label(window, bg="black", fg="yellow", text=cash, font="Times 25") ####cash
cashtext.pack()
cashtext.place(x=340, y=900)
####################################################


#bottom
char1_1 = Label(window, bg="black", fg="red", text=charstats[randomchar1], font="Times 12") ####suikastçı büyücü text
char1_1.pack()
char1_1.place(x=650, y=945)
cash1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
cash1 = cash1.resize((30, 15))
cash1 = ImageTk.PhotoImage(cash1)
cashalt1 = Label(window, image=cash1, border=False)
cashalt1.image = cash1
cashalt1.pack()
cashalt1.place(x=675,y=970)
cashprice1 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar1], font="Times 13") ####cash
cashprice1.pack()
cashprice1.place(x=663, y=965)
imgalt1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar1+".png")
imgalt1 = imgalt1.resize((100, 100))
imgalt1 = ImageTk.PhotoImage(imgalt1)
panelalt1 = Label(window, image=imgalt1, border=False)
panelalt1.image = imgalt1
panelalt1.pack()
panelalt1.place(x=630,y=847)
buy1button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy1)
buy1button.pack()
buy1button.place(x=628, y=990)
#############
char2_1 = Label(window, bg="black", fg="red", text=charstats[randomchar2], font="Times 12") ####suikastçı büyücü text
char2_1.pack()
char2_1.place(x=870, y=945)
cash2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
cash2 = cash2.resize((30, 15))
cash2 = ImageTk.PhotoImage(cash2)
cashalt2 = Label(window, image=cash2, border=False)
cashalt2.image = cash2
cashalt2.pack()
cashalt2.place(x=895,y=970)
cashprice2 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar2], font="Times 13") ####cash
cashprice2.pack()
cashprice2.place(x=883, y=965)
imgalt2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar2+".png")
imgalt2 = imgalt2.resize((100, 100))
imgalt2 = ImageTk.PhotoImage(imgalt2)
panelalt2 = Label(window, image=imgalt2, border=False)
panelalt2.image = imgalt2
panelalt2.pack()
panelalt2.place(x=850,y=847)
buy2button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy2)
buy2button.pack()
buy2button.place(x=848, y=990)
#############
char3_1 = Label(window, bg="black", fg="red", text=charstats[randomchar3], font="Times 12") ####suikastçı büyücü text
char3_1.pack()
char3_1.place(x=1090, y=945)
cash3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
cash3 = cash3.resize((30, 15))
cash3 = ImageTk.PhotoImage(cash3)
cashalt3 = Label(window, image=cash3, border=False)
cashalt3.image = cash3
cashalt3.pack()
cashalt3.place(x=1112,y=970)
cashprice3 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar3], font="Times 13") ####cash
cashprice3.pack()
cashprice3.place(x=1100, y=965)
imgalt3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar3+".png")
imgalt3 = imgalt3.resize((100, 100))
imgalt3 = ImageTk.PhotoImage(imgalt3)
panelalt3 = Label(window, image=imgalt3, border=False)
panelalt3.image = imgalt3
panelalt3.pack()
panelalt3.place(x=1070,y=847)
buy3button = Button(window, width=14 , bg="red", fg="white", border=False , text="Buy" , command=buy3)
buy3button.pack()
buy3button.place(x=1068, y=990)
#############
char4_1 = Label(window, bg="black", fg="red", text=charstats[randomchar4], font="Times 12") ####suikastçı büyücü text
char4_1.pack()
char4_1.place(x=1312, y=945)
cash4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/cash.png")
cash4 = cash4.resize((30, 15))
cash4 = ImageTk.PhotoImage(cash4)
cashalt4 = Label(window, image=cash4, border=False)
cashalt4.image = cash4
cashalt4.pack()
cashalt4.place(x=1334,y=970)
cashprice4 = Label(window, bg="black", fg="yellow", text=charcashs[randomchar4], font="Times 13") ####cash
cashprice4.pack()
cashprice4.place(x=1322, y=965)
imgalt4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/"+randomchar4+".png")
imgalt4 = imgalt4.resize((100, 100))
imgalt4 = ImageTk.PhotoImage(imgalt4)
panelalt4 = Label(window, image=imgalt4, border=False)
panelalt4.image = imgalt4
panelalt4.pack()
panelalt4.place(x=1290,y=847)
buy4button = Button(window, width=14, bg="red", fg="white", border=False , text="Buy" , command=buy4)
buy4button.pack()
buy4button.place(x=1288, y=990)
###################################################################

#statbox
stat1 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat1 = stat1.resize((100, 100))
stat1 = ImageTk.PhotoImage(stat1)
statalt1 = Label(window, image=stat1, border=False)
statalt1.image = stat1
statalt1.pack()
statalt1.place(x=430,y=657)
#############
stat2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat2 = stat2.resize((100, 100))
stat2 = ImageTk.PhotoImage(stat2)
statalt2 = Label(window, image=stat2, border=False)
statalt2.image = stat2
statalt2.pack()
statalt2.place(x=600,y=657)
#############
stat3 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat3 = stat3.resize((100, 100))
stat3 = ImageTk.PhotoImage(stat3)
statalt3 = Label(window, image=stat3, border=False)
statalt3.image = stat3
statalt3.pack()
statalt3.place(x=770,y=657)
#############
stat4 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat4 = stat4.resize((100, 100))
stat4 = ImageTk.PhotoImage(stat4)
statalt4 = Label(window, image=stat4, border=False)
statalt4.image = stat4
statalt4.pack()
statalt4.place(x=940,y=657)
#############
stat5 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat5 = stat5.resize((100, 100))
stat5 = ImageTk.PhotoImage(stat5)
statalt5 = Label(window, image=stat5, border=False)
statalt5.image = stat5
statalt5.pack()
statalt5.place(x=1110,y=657)
#############
stat6 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat6 = stat6.resize((100, 100))
stat6 = ImageTk.PhotoImage(stat6)
statalt6 = Label(window, image=stat6, border=False)
statalt6.image = stat5
statalt6.pack()
statalt6.place(x=1280,y=657)
#############
stat7 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat7 = stat7.resize((100, 100))
stat7 = ImageTk.PhotoImage(stat7)
statalt7 = Label(window, image=stat7, border=False)
statalt7.image = stat7
statalt7.pack()
statalt7.place(x=1450,y=657)
###################################################################

#statbox top
stat1_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat1_2 = stat1_2.resize((100, 100))
stat1_2 = ImageTk.PhotoImage(stat1_2)
statalt1_2 = Label(window, image=stat1, border=False)
statalt1_2.image = stat1_2
statalt1_2.pack()
statalt1_2.place(x=430,y=157)
#############
stat2_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat2_2 = stat2_2.resize((100, 100))
stat2_2 = ImageTk.PhotoImage(stat2_2)
statalt2_2 = Label(window, image=stat2_2, border=False)
statalt2_2.image = stat2_2
statalt2_2.pack()
statalt2_2.place(x=600,y=157)
#############
stat3_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat3_2 = stat3_2.resize((100, 100))
stat3_2 = ImageTk.PhotoImage(stat3_2)
statalt3_2 = Label(window, image=stat3_2, border=False)
statalt3_2.image = stat3_2
statalt3_2.pack()
statalt3_2.place(x=770,y=157)
#############
stat4_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat4_2 = stat4_2.resize((100, 100))
stat4_2 = ImageTk.PhotoImage(stat4_2)
statalt4_2 = Label(window, image=stat4_2, border=False)
statalt4_2.image = stat4_2
statalt4_2.pack()
statalt4_2.place(x=940,y=157)
#############
stat5_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat5_2 = stat5_2.resize((100, 100))
stat5_2 = ImageTk.PhotoImage(stat5_2)
statalt5_2 = Label(window, image=stat5_2, border=False)
statalt5_2.image = stat5_2
statalt5_2.pack()
statalt5_2.place(x=1110,y=157)
#############
stat6_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat6_2 = stat6_2.resize((100, 100))
stat6_2 = ImageTk.PhotoImage(stat6_2)
statalt6_2 = Label(window, image=stat6_2, border=False)
statalt6_2.image = stat6_2
statalt6_2.pack()
statalt6_2.place(x=1280,y=157)
#############
stat7_2 = Image.open("C:/Users/"+ username+ "/Desktop/minigame/statbox2.png")
stat7_2 = stat7_2.resize((100, 100))
stat7_2 = ImageTk.PhotoImage(stat7_2)
statalt7_2 = Label(window, image=stat7_2, border=False)
statalt7_2.image = stat7_2
statalt7_2.pack()
statalt7_2.place(x=1450,y=157)
###################################################################

#refresh
refreshbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Refresh |   2" , command=refresh)
refreshbutton.pack()
refreshbutton.place(x=1600,y=850)
#############
refreshcash = Image.open("C:/Users/"+ username+ "/Desktop/minigame/redcash.png")
refreshcash = refreshcash.resize((17, 17))
refreshcash = ImageTk.PhotoImage(refreshcash)
refreshcashalt = Label(window, image=refreshcash, border=False)
refreshcashalt.image = refreshcash
refreshcashalt.pack()
refreshcashalt.place(x=1685,y=852)
#############
fightbutton = Button(window, width=14, bg="red", fg="white", border=False , text="Fight" , command=fight)
fightbutton.pack()
fightbutton.place(x=1600,y=882)
###################################################################

#sell
sellbutton1 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell1)
sellbutton1.pack()
sellbutton1.place(x=430,y=767)
#############
sellbutton2 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell2)
sellbutton2.pack()
sellbutton2.place(x=600,y=767)
#############
sellbutton3 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell3)
sellbutton3.pack()
sellbutton3.place(x=770,y=767)
#############
sellbutton4 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell4)
sellbutton4.pack()
sellbutton4.place(x=940,y=767)
#############
sellbutton5 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell5)
sellbutton5.pack()
sellbutton5.place(x=1110,y=767)
#############
sellbutton6 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell6)
sellbutton6.pack()
sellbutton6.place(x=1280,y=767)
#############
sellbutton7 = Button(window, width=14, bg="purple", fg="white", border=False , text="Sell" , command=sell7)
sellbutton7.pack()
sellbutton7.place(x=1450,y=767)
###################################################################

#stats
stats2 = Label(window, bg="black", fg="red", text="Damage:", font="Times 16")
stats2.pack()
stats2.place(x=35, y=739)
###################################################################

window.mainloop()

