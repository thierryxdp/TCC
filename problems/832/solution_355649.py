def eh_quadrada(matriz):
    if matriz == [[]]:
        return True
    
    elif matriz!= [[]]:
        colunas = len(matriz[0])
        linhas = 0
        for x in matriz:
            linhas = linhas + 1
            if colunas == linhas:
                return True
            else:
                return False