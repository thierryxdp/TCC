def media_matriz(matriz):
    '''dada uma matriz, retorna a média de todos
    seus números
    list -> float'''
    med = 0
    k = 0
    for lin in matriz:
        for num in matriz:
			med += num
            k += 1
    return round(med/k, 2)