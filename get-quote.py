import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt","a")
  f.write("New Quote \n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(rnd)
    
  print(quotes[rnd], end = '')
  print(quotes[12])
if __name__=="__main__":
  primary()
 



