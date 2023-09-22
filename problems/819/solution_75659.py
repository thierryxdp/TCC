def filtraMultiplos(lista,numero):
    '''Calcula e retorna uma lista com os multiplos de um numero qualquer a partir de uma lista
       parameters:
       lista:lista original
       numero:numero qualquer usado para achar seus multiplos
    list,int->list'''
    proximo=0
    divisores=[]
    while proximo<len(lista):
        if lista[proximo]% numero == 0:
            divisores= divisores + [lista[proximo]]
        proximo=proximo+1
    return divisores