def insere(frase,n):
    lista = list(frase)
    n = str(n)
    lista.extend(n)
    lista.sort()
    return lista