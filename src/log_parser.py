import os, json
from pathlib import Path
#TODO Make a function for analysing a single run (first to parse it out, and then adding to WinIndex)
#The program writes a lot of empty spaces after finishing when run on the real run-log directory.
#This is probably caused by one of the many prints used for testing?
#Sorting wins in a winIndex-list with the index of won runs. This can then be used for calculating winrate, and keeping track of interesting runs. 


f = open("output.txt", "a")
#path = "C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs/THE_SILENT"
path = "C:/Users/92wiv/sts/src/data/logs"
AllRuns = []  
WinIndex = []

#Variable to determine how many runs to look at, should be input later
MaxNumberOfRuns = 10

#Prints out the content of a file in the current path-directory.
def read_text_file(file_path):
  try:
      with open(file_path, 'r') as f: 
            tmp = f.read()  #tmp is the JSON-object of a run
            AllRuns.append(tmp)
  except IOerror:
      print("Error reading file: " + file_path) 
      
      
#TODO this should probably just loop the directorys to read them in and add to AllRuns    
#Loops through a directory, and prints out all directorys through read_text_file()
def loop_directory(): 

  for file in os.listdir(path): 
      if(len(AllRuns) < MaxNumberOfRuns): #Reads in the requested amount of log-files. 
        os.chdir(path)
        
        # Check whether file is in text format or not 
        if file.endswith(".run"): 
            file_path = f"{path}/{file}"
            # call read text file function 
            read_text_file(file_path) 
      else:  
          break  
        
loop_directory()

#prints out the contents of a list
def print_out(lst):
  for x in range(len(lst)):
      print(lst[x])


print_out(AllRuns)
print("--------------------------------------")
print(AllRuns[1])


f.close()


#floor_reached":57