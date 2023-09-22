def conta_numero(numero, matriz):
    """Funcao que conta quantas vezes o numero fornecido aparece dentro da matriz fornecida;
    int, list(list) -> int"""
    
    contador = 0
    
    for linha in matriz:
        for elemento in linha:
            if numero == elemento:
                contador += 1
	return contador