def faltante(lista):
    '''descricao'''
    list.sort(lista)
    if lista[0]!=1:
        lista=list.insert(lista,0,1)
        return lista