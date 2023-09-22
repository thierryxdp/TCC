def repetidos(lista):
    ''' list -> int '''
    i = 1 
    resposta = 0
    while i < len(lista):
        if lista[i]==lista[i-1]:
            resposta = resposta + 1
            i = i + 1
    return resposta