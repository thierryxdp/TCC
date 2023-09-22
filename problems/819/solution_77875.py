def filtraMultiplo(lista, n):
    ''' list, int -> list '''
    i = 0
    resposta = []
    while i < len(lista):
        if lista[i]%n == 0:
            resposta = resposta + lista[i]
            i = i+1
    return resposta