def filtraMultiplos(lista,n):
    '''uma funcao que filtra uma lista usando um numero 'n' e retorna
    outra lista contendo todos os numeros filtrados'''
    i=0
    final = []
    while i < len(lista):
        if (lista[i]%n==0):
            list.append(final,lista[i])
            i += 1
        else:
            i += 1
    return final