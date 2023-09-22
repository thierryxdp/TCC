def conta_numero(numero,matriz):
    '''
    funcao que recebe um numero e uma matriz e retorna
    quantas veses esse numero aparece na matriz
    int, list -> int
    '''
    
    qtd = 0
    for num in [matriz]:
        if num == numero:
        	qtd += 1
        	return qtd