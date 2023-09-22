def filtraMultiplos(lista,n):
    ''' Recebe uma lista de números e um número n, e retorna outra lista contendo 
    todos os múltiplos de n na lista original. list, int -> list''' 
    M=[]
    i=0
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(M,lista[i])
        i+=1
    return M