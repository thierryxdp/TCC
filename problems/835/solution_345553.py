def melhor_volta(matriz):
    '''recebe a matriz e retorna o menor valor de tempo e em que qual volta ele foi atingido
    list(list) -> tup'''
    
    numero_teste = 10000000
    
    for i in range(len(matriz)):
        if numero_teste < i:
            numero_teste = i
            
    return (numero_teste,matriz[i])