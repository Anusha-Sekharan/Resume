import os
from datetime import datetime
JOURNAL_FILE="Digital_journal.txt"

def create():
  print("***** Digital Journal*****")
  print("1.Write new entry")
  print("2.View all entries")
  print("3.Exit")

def choice():
  user_choice=int(input("Enter your choice: "))
  return (user_choice)

def entry():
  print("***Welcome to new entry page***")
  j_entry=input("Enter your journal entry:")
  time=datetime.now()
  time_entry=f"[{time}]\n{j_entry}\n\n"
  handle=open("Digital_journal.txt","a")
  handle.write(time_entry)
  print("Journal entry saved")
  print("-----------------------------------------------------------")

def all_entry():
  print("***Welcome to view all entries page***")
  if os.path.exists(JOURNAL_FILE):
    handle=open(JOURNAL_FILE,"r")
    handle.seek(0,0)
    print(handle.read())
    print("---------------------------------------------------------")
  else:
    print("***No journal entry found***")

def aexit():
  print("***Thank you for using Digital Journal***")
  print("***Exitng the journal***")
  print("----------------------------------------------------------")

while True:
  create()
  user_choice=choice()
  if user_choice==1:
    entry()
  elif user_choice==2:
    all_entry()
  elif user_choice==3:
    aexit()
    break
  else:
    print("---Invalid choice---")
    print("---Use another choice---")
    create()
    choice()
