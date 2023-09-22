def filtraMultiplos(lista,n):
    '''Essa função filta os multiplos de um numero n,
    recebendo como entrada umaa lista de numeros e um numero,
    retornando uma outra lista com os elemtnos da lista original que 
    são divisiveis por n 
    list, float -> list'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i]%n == 0:
               lista1 = lista1 + (lista[i],)
               i = i + 1
               return list(lista1)