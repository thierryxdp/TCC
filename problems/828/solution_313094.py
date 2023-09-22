def primo(n):
    """Funcao calcula e retorna se um dado numero(n) e primo ou na0"""
    i=1
    pos=0
    for num in range(2,n):
        if n%i==0:
            pos+=1    
    if pos!=2:
        return False 
    else:
        return True