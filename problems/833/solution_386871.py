def conta_numero(numero,matriz):
    '''
    funcao que recebe um numero e uma matriz e retorna
    quantas veses esse numero aparece na matriz
    int, list -> int
    '''
    
    i = 0
    for num in matriz:
        qtd = 0
        for numero in matriz[i]:
            if num == numero:
        i += 1
        	qtd += 1
    return qtd