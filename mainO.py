import os

def display():
       print("press 1 to know the path of current directory")
       print("press 2 to make a new directory in the current path ")
       print("pres 3 to rename a directory ")
       print("press 4 to remove a directory")
       print("press 5 to quit from the running program")
              

def path_of_current_directory():
    curDir=os.getcwd()
    print("path is")
    print(curDir)


def new_directory():
    nd=os.mkdir("file-11")
    print("new directory is created only once ")

       

def rename_directory():
    rn=os.rename("file-11","file-22")
    print("file is renamed")
  
       
                     

def remove_directory():
    rmv=os.rmdir("file-22")
    print("file is removed")

def qu():
       print("exit from a file ")
       quit()
       



while True:
       display()
       ch=int(input("enter your choice!!!"))
       if(ch==1):
           path_of_current_directory()
       elif(ch==2):
           new_directory()
       elif(ch==3):
           rename_directory()
       elif(ch==4):
           remove_directory()
       elif(ch==5):
            qu()
       else:
              print("wrong choice!! press app. number")

