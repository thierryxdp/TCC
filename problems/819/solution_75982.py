def filtraMultiplos(lista,num):
    ''' essa funcao retorna os multiplos de um numero dado como
    entrada '''
    resposta = []
    indice = 0
    while indice < len(lista):
        if lista[indice]%num == 0:
            resposta.append(lista[indice])
        indice += 1
    return resposta