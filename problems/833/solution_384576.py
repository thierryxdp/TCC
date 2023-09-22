def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de
    tamanho qualquer, conta e retorna quantas vezes aquele número
    aparece na matriz
    int, list -> int'''
    
    soma = 0
    
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                soma = soma + 1
                
    return soma