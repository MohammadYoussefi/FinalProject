colleges = [
        "فنی و مهندسی",
        "علوم پایه",
        "علوم انسانی",
        "دامپزشکی",
        "اقتصاد",
        "کشاورزی",
        "منابع طبیعی"]


states = [
    "اراک", "ارومیه", "اردبیل", "اصفهان", "اهواز", "ایلام", "بجنورد", "بندرعباس",
    "بوشهر", "بیرجند", "تبریز", "تهران", "خرم‌آباد", "رشت", "زاهدان", 
    "زنجان","خرم آباد", "ساری", "سمنان", "سنندج", "شهرکرد", "شیراز", "قزوین",
    "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "مشهد", "همدان","خرم اباد"
    "یاسوج", "یزد"
]

subjects = [
        "مهندسی برق-الکترونیک",
        "مهندسی برق",
        " مهندسی شهرسازی",
        "مهندسی کامپیوتر",
        "مهندسی عمران",
        "مهندسی برق-قدرت",
        "مهندسی مکانیک",
        "مهندسی معدن",
        "مهندسی پلیمر"
]

Errors = {}

class Datavalidation:

    def check_STID(STID: int):
            count_student_number = 0
            StudentNumber_copy = STID
            while StudentNumber_copy > 0:
                L = StudentNumber_copy % 10
                count_student_number += 1
                StudentNumber_copy //= 10
            if count_student_number != 11:
                Errors["STID"] = "Student number must be 11 characters ! "
            elif count_student_number == 11:
                if 400 <= int(STID) // 100000000 <= 402:
                    if ((STID % 100000000) // 100) == 114150:
                        if 1 <= STID % 100 <= 99:
                            pass
                        else:
                            Errors["STID"] = "Invalid Student Number! (Index Error)"
                    else:
                        Errors["STID"] = "Invalid Student Number !"
                else:
                    Errors["STID"] = "Invalid Student Number ! (Year Error)"


    def check_FNAME(Fname: str):
            i = 0
            P_count = 0
            while i < len(Fname):
                if len(Fname) <= 10:
                    if 1568 <= ord(Fname[i]) <= 1610 or Fname[i] == "ی" or Fname[i] == "چ" or Fname[i] == "پ" or \
                            Fname[i] == "ک" or Fname[i] == "گ" or Fname[i] == "ژ" or Fname[i] == " ":
                        P_count += 1
                    else:
                        Errors["FName"] = "Fname Must be only Persian Characters ! "
                else:
                    Errors["FName"] = "Fname must be less than 10 Characters !"
                i += 1

            if P_count == len(Fname):
                pass
    

    def check_LNAME(Lname: str):
            i = 0
            P_count = 0
            while i < len(Lname):
                if len(Lname) <= 10:
                    if 1568 <= ord(Lname[i]) <= 1610 or Lname[i] == "ی" or Lname[i] == "چ" or Lname[i] == "پ" or \
                            Lname[i] == "ک" or Lname[i] == "گ" or Lname[i] == "ژ" or Lname[i] == " ":
                        P_count += 1
                    else:
                        Errors["LName"] = "Lname Must be only Persian Characters ! "
                else:
                    Errors["LName"] = "Lname must be less than 10 Characters !"
                i += 1

            if P_count == len(Lname):
                pass
    
    
    def check_FATHER(Father : str):
            i = 0
            P_count = 0
            while i < len(Father):
                if len(Father) <= 10:
                    if 1568 <= ord(Father[i]) <= 1610 or Father[i] == "ی" or Father[i] == "چ" or Father[i] == "پ" or \
                            Father[i] == "ک" or Father[i] == "گ" or Father[i] == "ژ" or Father[i] == " ":
                        P_count += 1
                    else:
                        Errors["FATHER"] = "Father Must be only Persian Characters ! "
                else:
                    Errors["FATHER"] = "Father must be less than 10 Characters !"
                i += 1

            if P_count == len(Father):
                pass

    
    def check_BIRTH(Birth : str):
        date_copy = Birth.split("/")
        if 1 <= int(date_copy[0]) <= 1402:
            if 1 <= int(date_copy[1]) <= 12:
                if 1 <= int(date_copy[2]) <= 31:
                    pass
                else:
                    Errors["BIRTH"] = "Ivalid Date ! (Day Error)"
            else:
                Errors["BIRTH"] = "Invalid Date ! (Month Error)"
        else:
            Errors["BIRTH"] = "Invalid Date ! (Year Error)"
        

    def check_IDS(IDS : str):
        count_num = 0
        count_letters = 0
        count_digits = 0

        if len(IDS) == 9:
                for j in range(0, 6):
                    if 48 <= ord(IDS[j]) <= 57:
                        count_num += 1
                        if count_num == 6:
                            if 1570 <= ord(IDS[6]) <= 1610 or IDS[6] == "ی" or IDS[6] == "ژ" or IDS[6] == "ک" \
                                    or IDS[6] == "پ" or IDS[6] == "گ" or IDS[6] == "چ":
                                count_letters += 1
                                if count_letters != 1:
                                    Errors["IDS"] = "Invalid IDS(سریال شناسنامه)"
        if len(IDS) == 9 and count_num == 6 and count_letters == 1:
            for k_serial in range(7, 9):
                if 48 <= ord(IDS[k_serial]) <= 57:
                    count_digits += 1

        if len(IDS) == 9 and count_num == 6 and count_letters == 1 and count_digits == 2:
            pass
        else:
            Errors["IDS"] = "Invalid IDS(سریال شناسنامه)"

    def check_BornCity(BornCity : str):
        p = 0
        for i in range(0,32):
            if BornCity == states[i]:
                p += 1

        if p != 0:
            pass
        else:
            Errors["BORNCITY"] = "Invalid BornCity !"
        

    def check_Address(Address: str):
        i = 0
        if len(Address) < 100:
            while i < len(Address):
                if 1568 <= ord(Address[i]) <= 1610 or Address[i] == "ی" or Address[i] == "چ" or Address[i] == "پ" or \
                        Address[i] == "ک" or Address[i] == "گ" or Address[i] == "ژ" or 47 < ord(Address[i]) < 58 or \
                            Address[i] == "-" or Address[i] == "." or Address[i] == " ":
                            pass
                else:
                    Errors["ADDRESS"] = "Invalid Address !"
                i += 1
        else:
            Errors["ADDRESS"] = "Invalid Address !"
        

    def check_POSTALCODE(PostalCode : int):
        count_digit = 0
        while PostalCode > 0:
            L = PostalCode // 10
            count_digit += 1
            PostalCode //= 10
        if count_digit == 10:
            pass
        else:
           Errors["POSTALCODE"] = "Invalid PostalCode !"
        

    def check_CPHONE(CPhone : str):
        count_num = 0
        if len(CPhone) == 11:
            if str(CPhone[0]) == "0":
                if str(CPhone[1]) == "9":
                    i = 2
                    while i < 11:
                        if 48 <= ord(CPhone[i]) <= 57:
                            count_num += 1
                        i += 1
                else:
                    Errors["CPHONE"] =  "Invalid CPhone Number !" 
            else:
                Errors["CPHONE"] = "Invalid CPhone Number !"
        else:
            Errors["CPHONE"] = "Invalid CPhone Number !"
        if len(CPhone) == 11:
            if count_num == 9:
                pass
            else:
                Errors["CPHONE"] = "Invalid CPhone Number !"
            

    def check_HPHONE(HPhone : int):
        count_land_line = 0
        land_line_copy = str(HPhone)
        i_land_line = 0
        while i_land_line < len(land_line_copy):
            if 48 <= ord(land_line_copy[i_land_line]) <= 57:
                count_land_line += 1
            i_land_line += 1
        if count_land_line == 8:
            pass
        else:
            Errors["HPHONE"] = "Invalid HPhone Number !"

    def check_MAJOR(Major : str):
        i = 0
        count_subject = 0
        while i < 9:
            if Major == subjects[i]:
                count_subject += 1
            i += 1
        if count_subject == 1:
            pass
        else:
            Errors["MAJOR"] = "Invalid Major !"
        
    def check_MARRIED(Married : str):
        if Married == "مجرد" or Married == "متاهل":
            if Married == "مجرد":
                pass
            else:
                pass
        else:
            Errors["MARRIED"] = "Invalid Married ! (مجرد یا متاهل)"
        

    def check_ID(ID : str):     
        for i in range(0, len(ID)):
            if 47 < ord(ID[i]) < 58:
                pass
            else:
                Errors["ID"] = "ID must be Only Integer !(کد ملی نادرست)"
        if len(ID) == 10:  
            L = len(ID)
            Sum = 0
            i = L 
            while i > 1:
                for j in range(0, L - 1):
                    Sum += i * int(ID[j])
                    i -= 1
            i = L - 1
            if (Sum % 11) < 2 :
                if (Sum % 11) == int(ID[i]):
                    pass
                else:
                    Errors["ID"] = "Invalid ID ! (کدملی نادرست)"
            else:
                if  11 - (Sum % 11) == int(ID[i]):
                    pass
                else:
                    Errors["ID"] = "Invalid ID ! (کدملی نادرست)"
        else:
            Errors["ID"] = "ID must be 10 characters ! (کدملی نادرست)"


    def check_CID(cid: str):
        if len(cid) != 5:
            Errors["CID"] = "cid must be 5 characters !"
        else:
            for i in range(0, len(cid)):
                if 47 < ord(cid[i]) < 58:
                    pass
                else:
                    Errors["CID"] = "cid must be only integer !"
                    

    def check_CNAME(cname: str):
        if len(cname) > 25:
            Errors["CName"] = "cname must be less than 25 characters !"
        else: 
            for i in range(0, len(cname)):
                if 1568 <= ord(cname[i]) <= 1610 or cname[i] == "ی" or cname[i] == "چ" or cname[i] == "پ" or \
                    cname[i] == "ک" or cname[i] == "گ" or cname[i] == "ژ" or cname[i] == " ":
                    pass
                else:
                    Errors["CName"] =  "cname must be only persian characters !"
   
    def check_DEPARTMENT(department: str):
        i = 0
        p = 0
        while i < 7:
            if department == colleges[i]:
                p += 1
            i += 1
        if p != 1:
                Errors["DEPARTMENT"] = "Invalid Department !"
               
    
    def chek_CREDIT(credit: int):
        if credit < 1 or credit > 4:
            Errors["CREDIT"] = "credit must be between 0 and 5 (0 < Credit < 5)"
            


    def check_LID(lid: str):
        if len(lid) != 6:
            Errors["LID"] = "LID must be 6 characters !"
        else:
            for i in range(0, len(lid)):
                if 47 < ord(lid[i]) < 58:
                    pass
                else:
                    Errors["LID"] = "LID must be only integer !"




