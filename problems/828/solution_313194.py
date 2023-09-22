def primo(inteiro):
    '''retorna true se inteiro for primo e, 
    false se nao for
    int -> bool'''
    
    j = 0
    
    for i in range(2,inteiro):
        if inteiro%i == 0:
            j += 1
            
    if j == 0:
        return True
    else:
        return False