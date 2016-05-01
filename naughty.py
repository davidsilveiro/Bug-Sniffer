#!/usr/bin/python
from sys import argv
from ftplib import FTP

               
    """ PHP User Suppulied Data Functions to enumerate againsts """

PHP_USER_SUP =['$_GET', '$_POST','$_COOKIE','$_REQUESTS', 
               '$_FILES','REQUEST_METHOD','QUERY_STRING',
               'REQUEST_URI', 'HTTP_ACCEPT','HTTP_ACCEPT\
                CHARSET','HTTP_ACCEPT_ENCODING','HTTP_AC\
                CEPT_LANGUAGE', 'HTTP_CONNECTION','HTTP_\
                HOST', 'HTTP_REFERER', 'HTTP_USER_AGENT',
               'PHP_SELF']

    """ Counter for line number in file after discovery """

line_Count = 0 

def main():

    """ Command line arguements, filename & options """
    
    try:
        with open(argv[1],"r\
        	") as file_Name:
            content = file_Name.read()

        if argv[2] == ("-P") or ("-p"):
            language = ("PHP")

        if argv[2] == ("-J") or ("-j"):
            language = ("JS")

    except TypeError:
    	print("Oops!")
    
    """ Enumerates through file & list and checks """
    """ for existance of func(function) in line   """
    """ (list), proceeds by stripping \r\n\ and   """
    """ printing line number ([str] turns int     """
    """	to string), line containing function,     """
    """ and the name of said function.            """

    for line in content:
    	for i, func in enumerate(PHP_USER_SUP):
    	    if func in line:

    	    new_Line = line.rstrip("\r\n")
            line_Count += 1
            
            print("%s) %s\n [%s]\
            "% (str(line_Count),new_Line, func)

    """ Else if statement returns false, continue """
    """ on by adding 1 onto line_Count.           """
        
            else:
        	    line_Count += 1
                pass

    print("Analysis Complete!\n              ")
    print("Would you like to save & report?\n")
    print(" Y or N\n                         ")

    Ans_Save = raw_input("Save: ").lower()
    Ans_Send = raw_input("Send: ").lower()

    try:
    	if Ans_Save == 'y':
            Ans_Dir = raw_input("Path: ")
            print("Saving...")

            #####NEEDS FINISHING HERE#####
#################################################################            
            print("Saved!")

        else:
        	Ans_Save = 'No'

        if Ans_Send == 'y':
           ip = raw_input("IP: ")
           userName = raw_input("username: ")
           userPass = raw_input("password: ")

        else:
        	Ans_Send == 'No'

    except TypeError:
    	print("Another Oops!")

    session = FTP(IP,userName,userPass)
    current_Dir = ftp.pwd()

    try:
    	with open('report.txt', 'rb\
    		') as report

    	###NEEDS FINISHING HERE######
#####################################################################

    except TypeError:
    	print("Stop breaking!")


    """ Start """

if __name__ == '__main__':
	main()
     
