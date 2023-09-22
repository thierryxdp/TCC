def primo(n):
    """int -> int"""
    """retorna True se for primo e False se não"""
    
    d = round(n**0.5) + 1
    q = 0
    
    for i in range(1,d):
        if n%i == 0:
            q += 1
            pass
        pass
    if n >=2 and q == 1:
        return True
    else:
        return False