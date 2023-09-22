def conta_numero(numero,matriz):
    ''' função que procura e calcula a quantidade de aparições
        do número fornecido dentro da matriz de entrada
        [int,list--> int]'''
    
    TOTAL = []
    soma = 0
    for sublista in matriz:
        for inteiro in sublista:
            if inteiro == numero:
                soma += 1
                list.append(TOTAL,soma)       
            
        
    return soma