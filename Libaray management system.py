'''
----Python program for Library Data Management System---
'''
import datetime                                                 #importing datetime module to this file
'''
----read function to read the data from the text file and store then in a list----
'''
def read():                                                     #creating a function called read
    file = open('Books.txt','r')                                #opening a file name "Books.txt" and reading the data on it
    lines = file.readlines()                                    #returning a list containing each line in the file as a list item
    file.close()                                                #closing the file--
    return lines                                                #returning the value of lines to the function


data=[]                                                         #declaring a list named data as global variable
for i in read():                                                ##iterating through the function read using for loop
    data.append(i.replace('\n',''). split(','))                 #replacing every \n (linespace) with empty string and spliting the list into dictonary where "," appears while iterating 
    
'''
-----display function to display the books and their details to the user------
'''
def display():
    print("Here are the list of books you can choose from :")   #printing the words inside (" ") in the terminal
    print()                                                     
    for i in range(6):                                          #running the loop 6 times fpr six books
            print("Book number :", data[i][4])                  #priting the name of the book from the dictonary
            print("The name of the book is :", data[i][0])
            print("The author is :",data[i][1])
            print("The number of books are :",data[i][2])
            print("The price of the book is :" ,data[i][3])
            print("----------------------------------------")
            print()
            
'''
-----borrowing function to let the user borrow books as they desire and update the number of books after they borrow----
'''
def borrowing():
    z=0
    cont = "y"                                                                              #storing String y in count as local variable
    while cont == "y":                                                                      #running the loop until the value of cont stays "y"
        try:                                                                                #the try function test a block of code to find errors if errors are found the except function is executed 
            opt1 = int(input("Which book do you want to borrow? Write the book number :"))  #asking the user to enter the book code for borrowing, changing the imput value into intiger and storing it
            if(opt1>5):
                print("Check the books details and write a valid value:")
            else:
                loop_one = "yes"
                while loop_one == "yes":
                    '''
                    ----Nested try catch---- 
                    '''
                    try: 
                        quantity = int(input("How many books of this name you want to borrow? :"))
                        loop_one = "no"
                    except:                                                                  #the except function is executed when the try block catches any errors to avoid errors and crashing of the program.
                        print("Enter a valid value1:")  
                name = input("Enter your name :")                                            #asking the user to Enter his/her name and store it in the variable name.  
                z+=1               
                t="Borrow-"+name+ str(z)+".txt"
                file = open(t,"w")                                                           #creating a file named before the borrower and writing data over it.
                file.write("Borrower name: "+ name + "\n")
                file.write("The book you borrowed is:"+ data[opt1][0] + "\n")
                file.write("The number of books you bowwowed is :" + str(quantity)+ "\n")    #writing the number of books borrowed by the user and converting the int "quanitity" to string using str() method        
                dollars_dec = int((data[opt1][3].strip('$')))                                #removing the $ sign from the string and returning the numeric value to dollars_dec using .strip method    
                file.write("Borrowed date :"+  str(datetime.datetime.now())+ "\n")           #writing the current date and time of book borrowed to the file using datetime module      
                file.write("The total amount is :"+ "$" + str(dollars_dec*quantity) + "\n" )
                file.write("Note: The book should be returned before 10 days of borrowing else fine of 10$ per day will be charged!!")
                print("Your data are written in the note")
                file.close() 
        
                '''
                ---Subratcting the numbers of books borrowed from the list and updating the list---
                '''
                y = int(data[opt1][2])
                last = y - quantity
                data[opt1][2] = last
                file = open("Books.txt","w")
                for i in range(6):                                      #running the loop 6 times and assigning the values of i from 0 to 5 respectively. 
                    for j in range(5):
                        file.write(str(data[i][j]))                     #updating the text file's data 
                        if j <5:
                            file.write(",")                             #writing commas if the value of j is less than 5
                        else:
                            file.write(" ")                             #replacing a "," with an empty string to avoid coammas before linebreak         
                    file.write('\n')
                file.close()
                '''
                -----Asking the user and running the loop as the users wishes -----
                '''
                opt2=input("Do you want to borrow any other books? press any key if yes and n if no :")
                if opt2 == "n":
                    cont = "n"                                           #if the user enters "n" setting the value of cont to "n" which will not allow the while loop to continue
        except:
            print("Enter a valid value3")
    return data

            
'''
-----return_ function to let the user return borrowed books as they desire and update the number of books after they return----
'''
def return_():
    cont = "y"
    while cont == "y":
        try:
            opt1 = int(input("Which book do you want to return? Write the book number :"))
            if(opt1>5):
                print("Check the books details and write a valid value:")
            else:
                loop_one = "yes"
                while loop_one == "yes":
                    try:    
                        quantity = int(input("How many books of this name you want to return? :"))
                        loop_one = "no"
                    except:
                        print("enter a valid value")
                name = input("Enter your name :")
                t="Return-"+name+".txt"
                file = open(t,"w")
                file.write("Returner name: "+ name + "\n")
                file.write("The book you returned is:"+ data[opt1][0] + "\n")
                file.write("The number of books you returned is :" + str(quantity)+ "\n")
                dollars_dec = int((data[opt1][3].strip('$')))
                file.write("Borrowed date :"+  str(datetime.datetime.now())+ "\n")
                '''
                ----Adding fine if the user dosen't retuns the books until 10 days of borrowing (rate $10 per day)----
                '''
                loop_two = "yes"
                while loop_two == "yes":
                    try:
                        charge = int(input("Enter the number of days passed u have borrowed the book?")+ "\n")
                        loop_two = "No"
                    except:
                        print("Enter a valid value")
                if(charge>10):
                    num = (charge - 10) * 10
                    file.write("As more than 10 days has passed the fine amount is :"+ "$"+str(num)+ "\n")
                    file.write("The total amount including fine is :"+ "$" + str(num + dollars_dec) + "\n" )
                else:
                    file.write("Congrats no fine allocated")
                    file.write("The total amount is :"+ "$" + str(dollars_dec) + "\n" )
                print("Your data are written in the note")
                file.close() 
                '''
                ---Adding the numbers of books returned from the user and rewriting the updated list---
                '''
                y = int(data[opt1][2])
                last = y + quantity
                data[opt1][2] = last
                file = open("Books.txt","w")
                for i in range(6):
                    for j in range(5):
                        file.write(str(data[i][j]))
                        if j <5:
                            file.write(",")
                        else:
                            file.write(" ")
                    file.write('\n')
                file.close()
                opt2=input("Do you want to return any other books? type y if yes and n if no :")
                if opt2 == "n":
                    cont = "n"
        except:
            print("Enter a valid value")
    return data

#-----main function to let the user choose through series of options as they desire:-----
def main():
    cont = "y"
    while cont == "y":
        '''
        Displaying the options menu to the user
        '''
        print("Welcome to Satish Library")
        print("--------------------------")
        print("Press 1 to Display the books")
        print("Press 2 to Borrow the books")
        print("Press 3 to Return the book")
        print("Press 4 to exit")
        ans = input("Enter a number for the above actions :")
        '''
        ----running the appropriate function as the user enters----
        '''
        if ans == "1":
            display()                                           
        elif ans == "2":
            borrowing()
        elif ans == "3":
            return_()
        elif ans =="4":
            print("Thank you for visiting")
            exit()
        else:
            print("Enter a valid value!!")
        abc = True
        '''
        -----Asking the user if they want to view the list again-----
        '''
        while abc == True:
            opt = input("Do you want to view the options again? press y to view or n to exit :")
            if opt == "n":
                print("Thank you for visiting")
                exit()
            elif opt == "y":
                abc = False
            else:
                print("Enter valid value")
'''
-----Running the main function-----
'''      
main()                                                             






