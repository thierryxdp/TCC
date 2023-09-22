def faltante(l):
    """Funcao calcula e retorna o numero faltante de uma lista; 
    int,int->int"""
    l.sort()
    posicao=1
    while posicao in l:
        posicao=posicao+1
    return posicao+1