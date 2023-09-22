def conta_numero(numero, matriz):
    contador = 0
    linhas_contadas = 0
    
    while linhas_contadas < len(matriz):
        for numero in matriz:
            linhas_contadas = linhas_contadas + 1
        contador = contador + 1
        
    return contador