def conta_numero(numero, matriz):
    """ Funcao que recebe um numero inteiro e um matriz de inteiros.
    	Retorna quantas vezes o numero apareceu na matriz;
        int, list -> int
    """
    numero_vezes_apareceu = 0
    for coluna in matriz:
        for linha in coluna:
            if linha == numero:
                numero_vezes_apareceu += 1
                
    return numero_vezes_apareceu