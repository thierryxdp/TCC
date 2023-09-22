def acima da media(lista,media):
    lista[0:0] = [media]
    list.sort(lista)
    maiores = lista[(list.index(lista,n))+1:]
    return maiores