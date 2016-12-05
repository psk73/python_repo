from __future__ import print_function
NUM_ROWS = 3
NUM_COLUMNS = 2
NUM_DASHES = 4

def main():
  '''
  Application to draw the grid using text chars 
  + and -. 
  '''
  for i in range(NUM_ROWS+1):
     for j in range(NUM_COLUMNS):
        print("+",end=" ")
        print("- "*NUM_DASHES,end="+")
        print("\n")
        if(i != NUM_ROWS+1): 
           for k in range(NUM_DASHES):
             print("| "*NUM_DASHES,end="|")
	     print("\n")
  return 

if __name__ == "__main__"
  main()
