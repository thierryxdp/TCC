def faltante(l):
    """Funcao calcula e retorna o numero faltante de uma lista; 
    int,int->int"""
    l.sort()
    posicao=1
    while l[posicao] in l: