def conta_numero(numero, matriz):
    '''
		Função que retorna quantas vezes aquele número aparece na matriz.
		Int,List => Int
    '''
    quantidade = 0
    for i in range(len(matriz)):
         quantidade += matriz[i].count(numero)
    return quantidade