def timeTable():
    table=int(input("Which times table would you like to use?")) #gets times table used
    numb=int(input("What number would you like to go up to?"))   #gets number to go up to
    for x in range(1,numb+1):                                    #iterates over times table
        print("{0} times {1} is {2}".format(table,x,table*x))    #prints times table and does math
    
timeTable()

