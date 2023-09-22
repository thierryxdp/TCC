def faltante(lista):
    '''Função que retorna qual número inteiro deste intervalo
    está faltando.
    lista=list->int'''
    list.sort(lista)
    x=0
    y=1
    while x<len(lista):
        if lista[x]==y:
            y=y+1
        x=x+1
    return y