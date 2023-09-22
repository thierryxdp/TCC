def insere(frase,n):
    lista = list(frase)
    num = list(n)
    lista.extend(num)
    lista.sort()
    return lista