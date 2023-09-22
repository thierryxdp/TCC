def insere(lista_numero,n):
    '''coment'''
    lista_numero[::1]=lista_numero
    lista1=lista_numero[0:-1]
    listas= [lista_numero]+[n]
    return listas