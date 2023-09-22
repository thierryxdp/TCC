def inverte(frase):
    lista=remove_pontuacao(frase)
    lista=str.lower(lista)
    lista=str.split(lista)
    list.reverse(lista)
    lista= str.join(' ', lista)
    return lista