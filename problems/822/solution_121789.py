def repetidos(lista):
    '''uma função que retorna o número  de vezes que um elemento é igual ao anterior'''
    resposta = 0
    contador = 0
    posicao = 0
    while contador < len(lista)-1:
        if lista[posicao] == lista[posicao+1]:
            resposta += 1
            contador =+1 
            posicao =+ 1
        else:    
            contador =1
            posicao =+ 1
    return resposta