import math
def qtd_divisores(n):
    div = int(n>0)
    for i in range(1,n+1):
        if n%i==0:
            div+=1
    return div

def primo(n):
    """
    Função que recebe um número n
    e retorna True se o número for primo
    e False caso contrário.
    
    int --> bool
    """
    raiz=math.sqrt(n)
    
    if qtd_divisores(raiz)>1:
        return False
    else:
        return True