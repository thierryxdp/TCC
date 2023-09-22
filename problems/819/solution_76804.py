def filtraMultiplos(lista,n):
    '''função que tendo como entyrada uma lista de numeros e um numero n 
    retorna uma lista com os numeros da lista original divisíveis por n
    list, int -> list'''
    l=()
    i=0
    while i < len(lista):
        if lista[i]%n:
            l= l + lista[i]
        i= i+1
    return l