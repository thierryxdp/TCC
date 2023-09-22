deffiltraMultiplos(lista,numero):
    """A funcao  recebe uma lista e um numero e retorna uma outra lista com os elementos que foram multiplos do numero.
    list, int -> list"""
    lista_nova=[]
    i=0
    while i<len(lista):
        if lista [i]%numero==0:
            list.insert(lista_nova,i,lista[i])
        i=i+1
    return lista_nova