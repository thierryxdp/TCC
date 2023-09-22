def pos(txt):
      i=1
      x=0
      while i<len(txt):
            if txt[i] == txt[i-1]:
                  x=x+1
                  print(x[i])
                  
      i+=1
      return x