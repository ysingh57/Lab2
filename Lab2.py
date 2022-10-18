#!/usr/bin/env pythn3
#impoting sys module in script
import sys

def cmd_args():
  name = str()
  course = str()
  
  name = sys.argv[1]
  course = sys.argv[2]
  
  print(f"factor1 = {name}")
  print(f"factor2 = {course}")
  print(f"Script: {sys.argv[0]}")
  print("Script and factors are : ", sys.argv[0], name, course)
  
 if __name__ == "__main__":
  cmd_args()
  
  
  
