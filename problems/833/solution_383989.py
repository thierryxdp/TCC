def conta_numero(numero, matriz):
    """Funcao que conta quantas vezes o numero fornecido aparece dentro da matriz fornecida;
    int, list(list) -> int"""
    
    contador = 0
    
    for linhas in matriz:
        for colunas in linhas:
            if numero == linhas[colunas]
            contador += 1
	return contador