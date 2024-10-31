def is_leap_year(year):

    isLeap = True 

    if year % 4 == 0:
        if year % 100 != 0:
            return isLeap == True
        elif year % 100 == 0:
            if year % 400 == 0:
                return isLeap == True
            else:
                return isLeap == False
    else:
        return isLeap == False
    
print(is_leap_year(1989))