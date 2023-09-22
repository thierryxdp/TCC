def filtraMultiplos(lista,numero):
    ''' funcao que dado uma lista e um numero retorna uma nova lista com os valores multiplos do numero da lista original
    list,int->list'''
    multiplos=[]
    x=0
    while x<len(lista):
        if lista[x]%numero==0:
            multiplos=multiplos+[lista[x]]
        x=x+1
    return multiplos