yeari = None
monthi = None
dayi = None
houri = None
minutei = None
secondi = None



while yeari == None:
    year = input("Enter year: ")
    # must be between 1900 and 2020
    try:
        yeari = int(year)
    except:
        pass

    if yeari is not None:
        
        if yeari < 1900:
            print("Year must be greater than 1900.")
            yeari = None
        elif yeari > 2020:
            print("Year must be less than 2020.")
            yeari = None
        else:
            print("Year is valid")
    else:
        print("Year "+year+" is invalid.")



while monthi == None:
    month = input("Enter month: ")
    # must be between 1 and 12
    try:
        monthi = int(month)
    except:
        pass
    if monthi is not None:
        if monthi < 1:
            print("Month must be greater 0.")
            monthi = None
        elif monthi > 12:
            print("Month must be less than 13.")
            monthi = None
        elif monthi < 10:
            # print("Month 0" + month + " is valid")
            month = "0" + month
        else:
            print("Month is valid")
    else:
        print("Month "+month+" is invalid.")



while dayi == None:
    day = input("Enter day: ")
    # must be between 1 and 31
    try:
        dayi = int(day)
    except:
        pass
    if dayi is not None:
        if dayi < 1:
            print("Day must be greater 0.")
            dayi = None
        elif dayi > 31:
            print("Day must be less than 32.")
            dayi = None
        elif dayi < 10:
            day = "0" + day
        else:
            print("Day is valid")
    else:
        print("Day "+day+" is invalid.")




while houri == None:
    hour = input("Enter hour: ")
    # must be between 1 and 24
    try:
        houri = int(hour)
    except:
        pass
    if houri is not None:
        if houri < 1:
            print("Hour must be greater 0.")
            houri = None
        elif houri > 24:
            print("Hour must be less than 25.")
            houri = None
        elif houri < 10:
            hour = "0" + hour
        else:
            print("Hour is valid")
    else:
        print("Hour "+hour+" is invalid.")



while minutei == None:
    minute = input("Enter minute: ")
    # must be between 1 and 59
    try:
        minutei = int(minute)
    except:
        pass
    if minutei is not None:
        if minutei < 1:
            print("Minute must be greater 0.")
            minutei = None
        elif minutei > 59:
            print("Minute must be less than 60.")
            minutei = None
        elif minutei < 10:
            minute = "0" + minute
        else:
            print("Minute is valid")
    else:
        print("Minute "+minute+" is invalid.")



while secondi == None:
    second = input("Enter second: ")
    # must be between 1 and 59
    try:
        secondi = int(second)
    except:
        pass
    if secondi is not None:
        if secondi < 1:
            print("Second must be greater 0.")
            secondi = None
        elif secondi > 59:
            print("Second must be less than 60.")
            secondi = None
        elif secondi < 10:
            second = "0" + second
        else:
            print("Second is valid")
    else:
        print("Second "+second+" is invalid.")

print (year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second) 