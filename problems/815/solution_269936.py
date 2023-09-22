def insere(lista,n):
    """insere um número ao final de uma lista e depois a organiza em forma crescente;
    string, int-> string"""
    l= lista
    n= [n]
    a= l+n
    resposta= a.sort()
    return resposta