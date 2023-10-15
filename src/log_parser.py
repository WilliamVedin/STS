import os




#Prints out the content of the file at an absolutely specified adress. 
def abs_reader():
  path = "C:/Users/92wiv/sts/src/data/logs/wins"
  os.chdir(path);
  file_path = "run1.run"
  
  with open(file_path, 'r') as f: 
        print(f.read()) 

  
  
test()