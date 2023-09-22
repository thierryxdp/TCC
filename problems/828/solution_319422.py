def primo(x):
    multipl=0
    
    for count in range(0,x):
        if (x % count == 0):
            multipl += 1
            
        elif(multipl == 0):
            x = True
            
        else:
            x = False
            
    return x