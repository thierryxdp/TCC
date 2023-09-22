def filtraMultiplos(lnumeros, n):
    '''Função que recebe uma lista de números lnumeros e um número, retornando outra lista;
    que contém todos os elementos da lista original que forem divisíveis por n;
    list, int -> list'''
    i = 0
    cnt = 0
    while i < len(lnumeros): 
            elementos = lnumeros[i]
            if lnumeros%n!=0:
                cnt +=1
            i +=1
    return cnt