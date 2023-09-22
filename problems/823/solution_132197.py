def faltante(lista):
    '''A função verificará qual é a numeração da peça que está faltando de um quebra-cabeça.
    Será inserida em uma lista os numeros da peças em ordem crescente e, caso ocorra uma quebra na sequência,
    a função retornará esse número.
    Dados de entrada -> list
    Dados de saída -> int'''
    
    Q = len(lista)
    i = 0
    
	if lista[0] != 1:
    	return lista[0] - 1
    
    while i < Q-1:
        if Q == 1 and lista[0] == 1:
            return lista[0] + 1
        
        elif Q > 1:
            if lista[i] != lista[i+1] - 1:
                return lista[i + 1] - 1
            
            i = i + 1
            
    return lista[-1] + 1