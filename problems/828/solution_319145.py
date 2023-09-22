def primo(n):
    
   
    for x in range(2, n):
        
        if (n % x) == 0:
            return False
        else:
            return True