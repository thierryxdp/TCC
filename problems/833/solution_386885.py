def conta_numero(numero,matriz):
    '''
    funcao que recebe um numero e uma matriz e retorna
    quantas veses esse numero aparece na matriz
    int, list -> int
    '''
    
    
    for num in matriz:
        qtd = 0
        i = 0
        if numero in matriz[i]:
            qtd +=  matriz[i].count(numero)
    		i += 1
        else:
            i += 1
        
    return qtd