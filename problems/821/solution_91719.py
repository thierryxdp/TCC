def fatorial(num):
    """Retorna a fatorial de num;
    int --> int"""
    
    iii = 0
    buffer = 1
    
    while (iii < num):
        buffer *= num - iii
        
        iii +=1
    
    return buffer