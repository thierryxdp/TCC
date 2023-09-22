def insere(lista,n):
    """insere um número ao final de uma lista e depois a organiza em forma crescente;
    string, int-> string"""
    l= lista
    a= list(n)
    b= l+a
    c= list.sort(b)
    return c