def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, a função conta e retorna para o usuário o número de
    vezes que o inteiro de entrada aparece na matriz.
    int, matriz -> int"""
    
    contador = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == 0:
        return contador
    
    elif linhas !=0:
        
    	for i in range(linhas):
        
        	for j in range(colunas):
            	candidato = matriz[i][j]
            
            	if candidato == numero:
                	contador +=1
                
    	return contador