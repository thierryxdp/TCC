def primo(n:int)-> bool:
    
    primos=0
    for i in range(2,n+1):
        if (n%i==0):
          return False
        else:
           return True