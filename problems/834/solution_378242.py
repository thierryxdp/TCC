def soma(n:list)-> float:
    '''Soma os elemntos de uma lista'''
    s=0
    for i in range(len(n)):
        s+= n[i]
    return s
def media_matriz(matriz:list)-> float:
    '''Calcula e retorna a média de todos os números da matriz recebida'''
    return round(sum(map(soma, matriz)) / (len(matriz) * len(matriz[0])),2)