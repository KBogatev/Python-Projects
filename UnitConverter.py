grouplist = [("Length"), ("Temperature"), ("Mass"), ("Quit")]
length = [("millimeters"), ("centimeters"), ("meters"), ("kilometers"), ("inches"), ("feet"), ("yards"), ("miles"), ("back")]
temperature = [("Kelvin"), ("Celsius"), ("Fahrenheit"), ("back")]
Weight = [("milligrams"),("grams"), ("kilograms"), ("pounds"), ("ounces"), ("back")]
retry = [("Try another Conversion"),("Quit")]
import sys
def mmTocm():
    global end
    end = start/10
    print(start,"Millimeters is", end, "Centimeters.")
def cmTomm():
    global end
    end = start*10
    print(start,"Centimeters is", end, "Millimeters.")
def mmTom():
    global end
    end = start/1000
    print(start,"Millimeters is", end, "Meters.")
def mTomm():
    global end
    end = start*1000
    print(start,"Meters is", end, "Millimeters.")
def mmTokm():
    global end
    end = start/1000000
    print(start,"Millimeters is", end,"Kilometers.")
def kmTomm():
    global end
    end = start*1000000
    print(start,"Kilometers is", end,"Millimeters.")
def mmToi():
    global end
    end = start/25.4
    print(start,"Millimeters is", end,"Inches.")
def iTomm():
    global end
    end = start*25.4
    print(start,"Inches is", end,"Millimeters.")
def mmTof():
    global end
    end = start/305
    print(start,"Millimeters is", end,"Feet.")
def fTomm():
    global end
    end = start*305
    print(start,"Feet is", end,"Millimeters.")
def mmToy():
    global end
    end = start/914
    print(start,"Millimeters is", end,"Yards.")
def yTomm():
    global end
    end = start*914
    print(start,"Yards is", end,"Millimeters.")
def mmTomi():
    global end
    end = start/1609344
    print(start,"Millimeters is", end,"Miles.")
def miTomm():
    global end
    end = start*1609344
    print(start,"Miles is", end,"Millimeters.")
def cmTom():
    global end
    end = start/100
    print(start,"Centimeters is", end,"Meters.")
def mTocm():
    global end
    end = start*100
    print(start,"Meters is", end,"Centimeters.")
def cmTokm():
    global end
    end = start/100000
    print(start,"Centimeters is", end,"Kilometers.")
def kmTocm():
    global end
    end = start*100000
    print(start,"Kilometers is", end,"Centimeters.")
def cmToi():
    global end
    end = start/2.54
    print(start,"Kilometers is", end,"Inches.")
def iTocm():
    global end
    end = start*2.54
    print(start,"Inches is", end,"Centimeters.")
def cmTof():
    global end
    end = start/30.48
    print(start,"Centimeters is", end,"Feet.")
def fTocm():
    global end
    end = start*30.48
    print(start,"Feet is", end,"Centimeters.")
def cmToy():
    global end
    end = start/91.44
    print(start,"Centimeters is", end,"Yards.")
def yTocm():
    global end
    end = start*91.44
    print(start,"Yards is", end,"Centimeters.")
def cmTomi():
    global end
    end = start/160934
    print(start,"Centimeters is", end,"Miles.")
def miTocm():
    global end
    end = start*160934
    print(start,"Miles is", end,"Centimeters.")
def mTokm():
    global end
    end = start/1000
    print(start,"Meters is", end,"Kilometers.")
def kmTom():
    global end
    end = start*1000
    print(start,"Kilometers is", end,"Meters.")
def mToi():
    global end
    end = start*39.37
    print(start,"Meters is", end,"Inches.")
def iTom():
    global end
    end = start/39.37
    print(start,"Inches is", end,"Meters.")
def mTof():
    global end
    end = start*3.281
    print(start,"Meters is", end,"Feet.")
def fTom():
    global end
    end = start/3.281
    print(start,"Feet is", end,"Meters.")
def mToy():
    global end
    end = start*1.094
    print(start,"Meters is", end,"Yards.")
def yTom():
    global end
    end = start/1.094
    print(start,"Yards is", end,"Meters.")
def mTomi():
    global end
    end = start/1609
    print(start,"Meters is", end,"Miles.")
def miTom():
    global end
    end = start*1609
    print(start,"Miles is", end,"Meters.")
def kmToi():
    global end
    end = start*39370
    print(start,"Kilometers is", end,"Miles.")
def iTokm():
    global end
    end = start/39370
    print(start,"Inches is", end,"Kilometers.")
def kmTof():
    global end
    end = start*3281
    print(start,"Kilometers is", end,"Feet.")
def fTokm():
    global end
    end = start/3281
    print(start,"Feet is", end,"Kilometers.")
def kmToy():
    global end
    end = start*1094
    print(start,"Kilometers is", end,"Yards.")
def yTokm():
    global end
    end = start/1094
    print(start,"Yards is", end,"Kilometers.")
def kmTomi():
    global end
    end = start/1.609
    print(start,"Kilometers is", end,"Miles.")
def miTokm():
    global end
    end = start*1.609
    print(start,"Miles is", end,"Kilometers.")
def iTof():
    global end
    end = start/12
    print(start,"Inches is", end,"Feet.")
def fToi():
    global end
    end = start*12
    print(start,"Feet is", end,"Inches.")
def iToy():
    global end
    end = start/36
    print(start,"Inches is", end,"Yards.")
def yToi():
    global end
    end = start*36
    print(start,"Yards is", end,"Inches.")
def iTomi():
    global end
    end = start/63360
    print(start,"Inches is", end,"Miles.")
def miToi():
    global end
    end = start*63360
    print(start,"Miles is", end,"Inches.")
def fToy():
    global end
    end = start/3
    print(start,"Feet is", end,"Yards.")
def yTof():
    global end
    end = start*3
    print(start,"Yards is", end,"Feet.")
def fTomi():
    global end
    end = start/5280
    print(start,"Feet is", end,"Miles.")
def miTof():
    global end
    end = start*5280
    print(start,"Miles is", end,"Feet.")
def yTomi():
    global end
    end = start/1760
    print(start,"Yards is", end,"Miles.")
def miToy():
    global end
    end = start*1760
    print(start,"Miles is", end,"Yards.")
def keToce():
    global end
    end = start - 273.15
    print(start,"Kelvin is", end, "Celsius.")
def ceToke():
    global end
    end = start + 273.15
    print(start,"Celsius is", end, "Kelvin.")
def keTofa():
    global end
    end = ((start - 273.15)*(9/5) + 32)
    print(start,"Kelvin is", end, "Fahrenheit")
def faToke():
    global end
    end = ((start - 32)*(5/9) + 273.15)
    print(start,"Fahrenheit is", end, "Kelvin.")
def ceTofa():
    global end
    end = (start * (9/5) + 32)
    print(start,"Celsius is", end,"Fahrenheit.")
def faToce():
    global end
    end = ((start - 32) * (5/9))
    print(start,"Fahrenheit is", end, "Celsius.")
def mgTog():
    global end
    end = start/1000
    print(start,"Milligrams is", end,"Grams.")
def gTomg():
    global end
    end = start*1000
    print(start,"Meters is", end,"Miles.")
def mgTokg():
    global end
    end = start/1000000
    print(start,"Milligrams is", end,"Kilograms.")
def kgTomg():
    global end
    end = start*1000000
    print(start,"Kilometers is", end,"Milligrams.")
def mgTolb():
    global end
    end = start/453592
    print(start,"Milligrams is", end,"Pounds.")
def lbTomg():
    global end
    end = start*453592
    print(start,"Pounds is", end,"Milligrams.")
def mgTooz():
    global end
    end = start/28350
    print(start,"Milligrams is", end,"Ounces.")
def ozTomg():
    global end
    end = start*28350
    print(start,"Ounces is", end,"Milligrams.")
def gTokg():
    global end
    end = start/1000
    print(start,"Grams is", end,"Kilograms.")
def kgTog():
    global end
    end = start*1000
    print(start,"Kilograms is", end,"Grams.")
def gtolb():
    global end
    end = start/454
    print(start,"Grams is", end,"Pounds.")
def lbTog():
    global end
    end = start*454
    print(start,"Pounds is", end,"Grams.")
def gTooz():
    global end
    end = start/28.35
    print(start,"Grams is", end,"Ounces.")
def ozTog():
    global end
    end = start*28.35
    print(start,"Ounces is", end,"Pounds.")
def kgTolb():
    global end
    end = start*2.205
    print(start,"Kilograms is", end,"Pounds.")
def lbTokg():
    global end
    end = start/2.205
    print(start,"Pounds is", end,"Kilograms.")
def kgTooz():
    global end
    end = start*35.274
    print(start,"Kilograms is", end,"Ounces.")
def ozTokg():
    global end
    end = start/35.274
    print(start,"Ounces is", end,"Kilograms.")
def lbTooz():
    global end
    end = start*16
    print(start,"Pounds is", end,"Ounces.")
def ozTolb():
    global end
    end = start/16
    print(start,"Ounces is", end,"Pounds.")
def retry_menu():
    i = 1
    for options in retry:
        print(i,'-',options)
        i = i + 1
    try:
        choice = int(input("Would you like to do another conversion or exit the menu?:"))
        if choice == 1:
            pass
        elif choice == 2:
            sys.exit()
        elif choice < 1 or choice > 2:
            wrong_input
            retry_menu()
    except ValueError:
        Error_message()
        retry_menu()
def converter_input():
    global start
    try:
        start = float(input("Input the value to be converted:"))
        converter_output()
    except ValueError:
        Error_message()
        converter_input()
def converter_output():
    if groups == 1:
        if unitl1 == 1 and unitl2 == 2:
            mmTocm()
        elif unitl1 == 2 and unitl1 == 1:
            cmTomm()
        elif unitl1 == 1 and unitl2 == 3:
            mmTom()
        elif unitl1 == 3 and unitl2 == 1:
            mTomm()
        elif unitl1 == 1 and unitl2 == 4:
            mmTokm()
        elif unitl1 == 4 and unitl2 == 1:
            kmTomm()
        elif unitl1 == 1 and unitl2 == 5:
            mmToi()
        elif unitl1 == 5 and unitl2 == 1:
            iTomm()
        elif unitl1 == 1 and unitl2 == 6:
            mmTof()
        elif unitl1 == 6 and unitl2 == 1:
            fTomm()
        elif unitl1 == 1 and unitl2 == 7:
            mmToy()
        elif unitl1 == 7 and unitl2 == 1:
            yTomm()
        elif unitl1 == 1 and unitl2 == 8:
            mmTomi()
        elif unitl1 == 2 and unitl2 == 3:
            cmTom()
        elif unitl1 == 3 and unitl2 == 2:
            mTocm()
        elif unitl1 == 2 and unitl2 == 4:
            cmTokm()
        elif unitl1 == 4 and unitl2 == 2:
            kmTocm()
        elif unitl1 == 2 and unitl2 == 5:
            cmToi()
        elif unitl1 == 5 and unitl2 == 2:
            iTocm()
        elif unitl1 == 2 and unitl2 == 6:
            cmTof()
        elif unitl1 == 6 and unitl2 == 2:
            fTocm()
        elif unitl1 == 2 and unitl2 == 7:
            cmToy()
        elif unitl1 == 7 and unitl2 == 2:
            yTocm()
        elif unitl1 == 2 and unitl2 == 8:
            cmTomi()
        elif unitl1 == 8 and unitl2 == 2:
            miTocm()
        if unitl1 == 3 and unitl2 == 4:
            mTokm()
        elif unitl1 == 4 and unitl1 == 3:
            kmTom()
        elif unitl1 == 3 and unitl2 == 5:
            mToi()
        elif unitl1 == 5 and unitl2 == 3:
            iTom()
        elif unitl1 == 3 and unitl2 == 6:
            mTof()
        elif unitl1 == 6 and unitl2 == 3:
            fTom()
        elif unitl1 == 3 and unitl2 == 7:
            mToy()
        elif unitl1 == 7 and unitl2 == 3:
            yTom()
        elif unitl1 == 3 and unitl2 == 8:
            mTomi()
        elif unitl1 == 8 and unitl2 == 3:
            miTom()
        elif unitl1 == 4 and unitl2 == 5:
            kmToi()
        elif unitl1 == 5 and unitl2 == 4:
            iTokm()
        elif unitl1 == 4 and unitl2 == 6:
            kmTof()
        elif unitl1 == 6 and unitl2 == 4:
            fTokm()
        elif unitl1 == 4 and unitl2 == 7:
            kmToy()
        elif unitl1 == 7 and unitl2 == 4:
            yTokm()
        elif unitl1 == 4 and unitl2 == 8:
            kmTomi()
        elif unitl1 == 5 and unitl2 == 6:
            iTof()
        elif unitl1 == 6 and unitl2 == 5:
            fToi()
        elif unitl1 == 5 and unitl2 == 7:
            iToy()
        elif unitl1 == 7 and unitl2 == 5:
            yToi()
        elif unitl1 == 5 and unitl2 == 8:
            iTomi()
        elif unitl1 == 8 and unitl2 == 5:
            miToi()
        elif unitl1 == 6 and unitl2 == 7:
            fToy()
        elif unitl1 == 7 and unitl2 == 6:
            yTof()
        elif unitl1 == 6 and unitl2 == 8:
            fTomi()
        elif unitl1 == 8 and unitl2 == 6:
            miTof()
        elif unitl1 == 7 and unitl2 == 8:
            yTomi()
        elif unitl1 == 8 and unitl2 == 7:
            miToy()
    elif groups == 2:
        if unitl1 == 1 and unitl2 == 2:
            keToce()
        elif unitl1 == 2 and unitl2 == 1:
            ceToke()
        elif unitl1 == 1 and unitl2 == 3:
            keTofa()
        elif unitl1 == 3 and unitl2 == 1:
            faToke()
        elif unitl1 == 2 and unitl2 == 3:
            ceTofa()
        elif unitl1 == 3 and unitl2 == 2:
            faToce()
    elif groups == 3:
        if unitl1 == 1 and unitl2 == 2:
            mgTog()
        elif unitl1 == 2 and unitl1 == 1:
            gTomg()
        elif unitl1 == 1 and unitl2 == 3:
            mgTokg()
        elif unitl1 == 3 and unitl2 == 1:
            kgTomg()
        elif unitl1 == 1 and unitl2 == 4:
            mgTolb()
        elif unitl1 == 4 and unitl2 == 1:
            lbTomg()
        elif unitl1 == 1 and unitl2 == 5:
            mgTooz()
        elif unitl1 == 5 and unitl2 == 1:
            ozTomg()
        elif unitl1 == 2 and unitl2 == 3:
            gTokg()
        elif unitl1 == 3 and unitl2 == 2:
            kgTog()
        elif unitl1 == 2 and unitl2 == 4:
            gtolb()
        elif unitl1 == 4 and unitl2 == 2:
            lbTog()
        elif unitl1 == 2 and unitl2 == 5:
            gTooz()
        elif unitl1 == 5 and unitl2 == 2:
            ozTog()
        elif unitl1 == 3 and unitl2 == 4:
            kgTolb()
        elif unitl1 == 4 and unitl2 == 3:
            lbTokg()
        elif unitl1 == 3 and unitl2 == 5:
            kgTooz()
        elif unitl1 == 5 and unitl2 == 3:
            ozTokg()
        elif unitl1 == 4 and unitl2 == 5:
            lbTooz()
        elif unitl1 == 5 and unitl2 == 4:
            ozTolb()
    retry_menu()

def menu_groups():
    i = 1
    for group in grouplist:
        print(i,'-',group)
        i = i + 1
def menu_length():
    i = 1
    for lenunit in length:
        print(i,'-',lenunit)
        i = i + 1
    global unitl1
    try:
        unitl1 = int(input("Select the unit you would like to convert from:"))
        if (0 < unitl1 <= 8):
            converting_unit()
        elif unitl1 == 9:
            menu_groups()
            Groups()
        elif unitl1 < 1 or unitl1 > 9:
            wrong_input()
            menu_length()
    except ValueError:
        Error_message()
        menu_length()
def menu_temperature():
    i = 1
    for tempunit in temperature:
        print(i, '-', tempunit)
        i = i + 1
    global unitl1
    try:
        unitl1 = int(input("Select the unit you would like to convert from:"))
        if (0 < unitl1 <= 3):
            converting_unit()
        elif unitl1 == 4:
            menu_groups()
            Groups()
        elif unitl1 < 1 or unitl1 > 4:
            wrong_input()
            menu_temperature()
    except ValueError:
        Error_message()
        menu_temperature()
def menu_weight():
    i = 1
    for weiunit in Weight:
        print(i,'-',weiunit)
        i = i + 1
    global unitl1
    try:
        unitl1 = int(input("Select the unit you would like to convert from:"))
        if (0 < unitl1 <= 5):
            converting_unit()
        elif unitl1 == 6:
            menu_groups()
            Groups()
        elif unitl1 < 1 or unitl1 > 6:
            wrong_input()
            menu_weight()
    except ValueError:
        Error_message()
        menu_weight()

def converting_unit():
    global unitl2
    try:
        unitl2 = int(input("Select the unit you are converting to:"))
        if groups == 1:
            if unitl2 != unitl1:
                if (0 < unitl2 <= 8):
                    converter_input()
                elif unitl2 == 9:
                    menu_length()
                elif unitl2 < 1 or unitl2 > 9:
                    wrong_input()
            else:
                wrong_input()
                converting_unit()
        if groups == 2:
            if unitl2 != unitl1:
                if (0 < unitl2 <= 3):
                    converter_input()
                elif unitl2 == 4:
                    menu_temperature()
                elif unitl2 < 1 or unitl2 > 4:
                    wrong_input()
            else:
                wrong_input()
                converting_unit()
        if groups == 3:
            if unitl2 != unitl1:
                if (0 < unitl2 <= 5):
                    converter_input()
                elif unitl2 == 6:
                    menu_weight()
                elif unitl2 < 1 or unitl2 > 6:
                    wrong_input()
            else:
                wrong_input()
                converting_unit()
    except ValueError:
        Error_message()
        converting_unit()       
def wrong_input():
    print("You didn't pick one of the options.")
def Error_message():
    print("Not valid.") 
def Groups():
    global groups
    try:
        groups = int(input("Type the number corresponding to the group of units you want to convert between:"))
    except ValueError:
        Error_message()
        menu_groups()
        Groups()
    if groups == 1:
        menu_length()
    elif groups == 2:
        menu_temperature()
    elif groups == 3:
        menu_weight()
    if groups == 4:
        sys.exit()
    elif groups < 1 or groups > 4:
        wrong_input() 
        Groups()
def program():
        menu_groups()
        Groups()
global isRunning
isRunning = (1 == True)
print("Hello, welcome to Konstantin's converter.")
while isRunning == True:
    program()





