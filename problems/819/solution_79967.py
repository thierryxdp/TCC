def filtraMultiplos(lista,numero):
    '''recebe uma lista e retorna uma nova lista com os multiplos
    do número determinado presentes na lista original
    list,int->list'''
    i=0
    listanova=[]
    while i<len(lista):
        if lista[i]%numero==0:
            listanova=list.extend(listanova,lista[i])
        i=i+1
    return listanova