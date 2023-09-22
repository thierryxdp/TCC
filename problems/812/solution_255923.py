def inverso(frase):
    lista = str.split(frase)
    lista.reverse(lista)
    return str.join(' ',lista)