def media_matriz(m):
    '''
    	Funcao que dada uma matriz de inteiros nao vazia, retorna a 
        media de todos os numeros da matriz, com duas casas decimais.
        list -> int
    '''
    dividendo = 0
    divisor = 0 
    for i in range(len(m)):
    	for j in range(len(m[i])):
            dividendo += m[i][j]
            divisor += 1   
    return round(dividendo/divisor, 2)