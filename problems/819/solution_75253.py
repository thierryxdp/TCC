def filtraMultiplos (lista,n):
    '''Essa função filtra os multiplos de um determinado numreo n
    , recebendo uma lista de numeros e um numero e retornar outras lia
    contendo todos os elementos da lista original que são divisiveis por n
    list, float -> list'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i]%n == 0:
               lista1 = lista1 + (lista[i],)
               i= i + 1
               return list(lista1)