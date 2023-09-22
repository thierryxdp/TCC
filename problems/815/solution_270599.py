def insere(frase,n):
    lista = list(frase)
    n = list(n)
    lista.extend(n)
    lista.sort()
    return lista