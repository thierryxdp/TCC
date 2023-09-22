def primo(x):
    multipl=0
    
    for count in range(2,x):
        if (x % count == 0):
            multipl += 2
            
        elif(multipl == 0):
            x = True
            
        else:
            x = False
            
    return x