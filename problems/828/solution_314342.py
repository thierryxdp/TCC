def primo(n:int)-> bool:
    
    for i in range(1,n+1):
        if not(n%i):
          return False
        else:
           return True