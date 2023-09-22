def insere(lista_numero,n):
    """insere um numero 'n' e deixa a lista de forma crescente;
    string, int -> tupla"""
    x = lista_numero
    y = str(n)
    w = x.append(y)
    z = list.sort(w)
    return z