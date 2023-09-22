def repetidos(lista):
    '''Recebe uma lista de números e retorna quantas vezes um elemento da lista é igual ao elemento anterrior'''
    anterior=0
    proximo=1
    resposta=0
    while proximo<len(lista):
        if lista[anterior]==lista[proximo]:
            resposta=resposta+1
        proximo=proximo+1
        anterior=anterior+1
    return resposta