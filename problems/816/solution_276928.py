def maiores(lista_numero,n):
    '''coment'''
    lista=lista_numero[:]+[n]
    resolucao=list.sort(lista)
    if n>lista_numero:
        return lista