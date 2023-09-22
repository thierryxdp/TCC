def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    
    for i in range (len(matriz)):
    	for j in range (len(matriz[0])):
            if a[i][j] == numero:
            	contagem.append(a[i][j])
    return len(contagem)