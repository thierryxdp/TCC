def primo(x,n):
    multipl=0
    
    for count in range(2,n):
        if (n % count == 0):
            multipl += 1
            
        elif(multipl == 0):
            x = True
            
        else:
            x = False
            
    return x