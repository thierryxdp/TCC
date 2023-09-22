def insere(frase,n):
    lista = list(frase)
    num = list(n)
    lista.extend(num)
    list.sort(lista)
    return lista