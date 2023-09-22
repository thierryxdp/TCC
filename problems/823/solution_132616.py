def faltante(l):
    """Funcao calcula e retorna o numero faltante de uma lista; 
    int,int->int"""
    l.sort()
    posicao=1
    i=1
    while posicao in l:
        if posicao+1==l[i]:
            posicao=posicao+1
    return posicao+1