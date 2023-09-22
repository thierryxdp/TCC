def conta_numero(numero,matriz):
    '''
    funcao que recebe um numero e uma matriz e retorna
    quantas veses esse numero aparece na matriz
    int, list -> int
    '''
    
    qtd = 0
    for num in matriz:
        i = 0   
        for i in range(len(matriz)):
            if numero in matriz[i]:
                i += 1
        qtd +=  matriz[i-1].count(numero)
    			   		
        
    	return qtd