def maiores(lista,N):
    '''Essa Funcao dada uma lista de numeros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n;
    Recebe uma lista de numeros e um numero inteiro n;
    Retorna outra lista, que contenha todos os numeros da lista original maiores que n.'''
    listafinal=[]
    for i in range(len(lista)):
        if(lista[i]>N):
            listafinal.append(lista[i])
    list.sort(listafinal)        
    return listafinal