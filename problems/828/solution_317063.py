def primo(num):
    
    for i in range(2,num):
        
        if num%i==0:
            return False
        
        if num/i==i:
            return False
        
        else:
            return True