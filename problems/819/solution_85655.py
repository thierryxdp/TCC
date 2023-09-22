def filtraMultiplos(listanum,num):
    '''Recebe uma lista de numeros e um numero e retorna outra 
    lista contendo todos os elementos da original que sao
    divisiveis pelo numero'''
    '''list,int->list'''
    listanova=[]
    i=0
    while i<len(listanum):
        if listanum[i]%num==0:
            listanova=listanova+[listanum[i],]
        i=i+1
    return listanova