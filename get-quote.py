import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read().splitlines()
  f.close()

  last = len(quotes) - 1
  rnd1, rnd2 = random.randint(0, last), random.randint(0, last)
  print(quotes[rnd1])
  print(quotes[rnd2])

if __name__== "__main__":
  primary()
