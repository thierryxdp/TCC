def primo(n):
    """Funcao calcula e retorna se um dado numero(n) e primo ou nao;
    int->bool"""
    i=1
    pos=0
    for num in range(n):
        if n%i==0:
            pos=pos+1
        i=i+1
    if pos!=2:
        return False 
    else:
        return True