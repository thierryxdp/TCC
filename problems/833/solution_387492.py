def conta_numero(numero, matriz):
    """Função que conta quantas vezes um número aparece dentro de uma matriz;
    Float, List(list) -> Int"""
    
    resultado = 0
    
    for lista in matriz:
        for x in lista:
            if x == numero:
                resultado = resultado + 1
	return resultado