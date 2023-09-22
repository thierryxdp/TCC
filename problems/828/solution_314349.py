def primo(n:int)-> bool:
    
    for i in range(2,n):
        if not(n%i):
          return False
        else:
           return True