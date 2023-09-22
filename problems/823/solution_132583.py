def faltante(l):
    """Funcao calcula e retorna o numero faltante de uma lista; 
    int,int->int"""
    l=()
    posicao=1
    i=1
    while i in l:
        if posicao==l[posicao]:
            posicao=posicao+1
    return posicao