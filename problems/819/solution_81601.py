def filtraMultiplos(lnumeros, n):
    '''Função que recebe uma lista de números lnumeros e um número, retornando outra lista;
    que contém todos os elementos da lista original que forem divisíveis por n;
    list, int -> list'''
    i = 0
    pares =[]
    while i < len(lnumeros): 
            if lnumeros[i]%n==0:
                pares = pares + [lnumeros[i],]
            i +=1
    return pares