import os, json
from pathlib import Path
#TODO
#The program writes a lot of empty spaces after finishing when run on the real run-log directory.
#This is probably caused by one of the many prints used for testing?

f = open("output.txt", "a")
#path = "C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs/THE_SILENT"
path = "C:/Users/92wiv/sts/src/data/logs"
AllRuns = []  

#Variable to determine how many runs to look at
MaxNumberOfRuns = 10

#Prints out the content of a file in the current path-directory.
def read_text_file(file_path):
  with open(file_path, 'r') as f: 
        tmp = f.read()
        AllRuns.append(tmp)
        print(tmp)
        
        
#Loops through a directory, and prints out all directorys through read_text_file()
def loop_directory(): 
  #print("path is --------" + path)
  #print(os.listdir(path))
  RunsInDir = 0
  
  #Determines number of runs in directory
  for file in os.listdir(path):
      if file.endswith(".run"):
          RunsInDir += 1
          
  print(RunsInDir)
  for file in os.listdir(path): 
      
      os.chdir(path)
      # Check whether file is in text format or not 
      if file.endswith(".run"): 
          file_path = f"{path}/{file}"
          
  
          # call read text file function 
          read_text_file(file_path) 
        
#testcase
loop_directory()

def print_outout():
  print("before allRuns - ")
  for x in range(len(AllRuns)):
      print(AllRuns[x], file=f)
  print("after allRuns - ")

print_outout()

f.close()



#floor_reached":57