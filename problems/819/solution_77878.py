def filtraMultiplos(lista, n):
    ''' list, int -> list '''
    i = 0
    resposta = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(resposta, lista[i])
            i = i+1
    return resposta