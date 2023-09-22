def insere(lista,n):
    """insere um número ao final de uma lista e depois a organiza em forma crescente;
    string, int-> string"""
    l= lista
    a= int(l)
    b= list((a,n))
    c= list.sort(b)
    return c