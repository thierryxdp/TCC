def inverte(frase):
    lista = str.split(frase)
    lista = list.reverse(lista)
    lista = str.join(' ',lista)
    return lista