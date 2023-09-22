def filtraMultiplos(lista,n):
    '''funcao que dada uma lista e um numero n retorna uma nova lista com os multiplos de n. list,int -> list'''
    nova_lista=[]
    indice=0
    while indice < len(lista):
        if lista[indice]%n == 0:
        nova_lista += [lista[indice]]
    return nova_lista