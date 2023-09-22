def repetidos(lista):
    '''
    valor de entrada:
    valor de saída:  '''
    proximo=0
    resposta=[]
    while proximo<len(lista):
        if proximo==proximo+1:
            resposta.append(1)
        proximo= proximo+1
        
    return sum(resposta)