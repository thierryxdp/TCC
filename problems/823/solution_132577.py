def faltante(l):
    """Funcao calcula e retorna o numero faltante de uma lista; 
    int,int->int"""
    l=()
    posicao=1
    while posicao in l:
        if posicao+1==l[posicao]:
            posisao=posicao+1
    return posicao