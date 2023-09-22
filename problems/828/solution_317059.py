def primo(num):
    
    for i in range(2,num):
        
        if num%i==0 or (i*i)==num:
            return False
        
        else:
            return True