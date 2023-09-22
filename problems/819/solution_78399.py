def filtraMultiplos (lista,numeros):
    '''função que recebe uma lista de número e um número 
    como entrada e retorne outra lista contendo todos 
    os números divisíveis pelo número dado.
    list, int -> list'''
    listafinal = []
    proximo = 0
    
    while proximo <len(lista):
        if lista[proximo]%numeros == 0:
            listafinal = listafinal + [lista[proximo],]
        proximo = proximo + 1
    return listafinal