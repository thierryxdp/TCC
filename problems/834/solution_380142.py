def media_matriz(m):
    '''
    	Função que dada uma matriz de inteiros não vazia,
        retorna a média de todos os números da matriz.
        OBS:Com exatamente duas casas decimais de precisão.
        contador:int
        acumulador:int
        i:int
        j:int
        return:float
    '''
    contador = 0
    acumulador = 0
    i = 0
    j = 0
    if len(m) != 0:
        while i < len(m):
            j = 0
            while j < len(m[i]):
                acumulador += m[i][j]
                contador += 1
                j += 1
            i += 1
        return round((acumulador / contador), 2)