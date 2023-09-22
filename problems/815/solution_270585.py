def insere(frase,n):
    lista = list(frase)
    n = str(n)
    lista.extend(n)
    list.sort(lista)
    return lista