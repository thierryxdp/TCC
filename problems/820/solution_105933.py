def posLetra(x,y,z):
    n=0
    p=1
    while n<len(x):
        if x[n]==y:
           if p<z:
             
              if n==(x.lastIndexOf(y)):
                  return -1
              p=p+1
           elif p==z:
              return n
           

        elif x[n]!=y:
          
            n=n+1