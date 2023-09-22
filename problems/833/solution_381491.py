def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    
    for linha in range (len(matriz)):
    	for coluna in range (len(matriz[0])):
            if matriz[linha][coluna] == numero:
            	contagem.append(matriz[linha][coluna])
    return len(contagem)