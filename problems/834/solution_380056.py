def media_matriz(matriz):
    ''' Retorna a média de todos os numeros de uma determinada (matriz) 
    list -> float'''
    todos_numeros = []
    
    for i in matriz:
        for i2 in i:
            todos_numeros.append(i2)

	return round(sum(todos_numeros) / len(todos_numeros), 2)