def filtraMultiplos (l,n):
    '''função que recebe uma lista de número e um número 
    como entrada e retorne outra lista contendo todos 
    os números divisíveis pelo número dado.
    list, int -> list'''
    listafinal = []
    proximo = 0
    
    while proximo <len(l):
        if l[proximo]%n == 0:
            listafinal = listafinal + (l[proximo],)
        proximo = proximo + 1
    return listafinal