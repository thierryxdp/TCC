def primo(x):
    
    
    
    for x in range(1,101):
        cont = 0
        for y in range(1,x+1):
            if x%y==0:
                return False
        if cont<=2:
            return True