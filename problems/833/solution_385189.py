def conta_numero(numero,matriz):
    
    """ Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    """"
    
    contador = 0
    
    for lin in range(0,len(matriz)):
        
        for col in range(0,len(matriz[lin])):
            
            if numero == matriz[lin][col]:
                
                countador += 1
                
    return countador