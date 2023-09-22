def conta_numero(numero,matriz):
    '''funcao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele numero aparece na matriz int, list -> list'''
    
    repeticoes = 0
    
     for coluna in matriz:
            
        for elemento in coluna:
            
            if elemento == numero:
                
                repeticoes = repeticoes + 1

    return repeticoes