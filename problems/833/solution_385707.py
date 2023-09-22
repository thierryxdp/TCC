def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros
    	de tamanho qualquer, conta e retorna quantas vezes aquele 
        numero aparece na matriz
        
        int, list(list) -> int'''
    
    acumulador = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                acumulador = acumulador + 1
    return acumulador