def media_matriz(matriz):
    '''dada uma matriz, retorna a média de todos
    seus números
    list -> float'''
    med = []
    for lin in matriz:
        for num in matriz:
			med.append(num)
    return round(sum(med)/len(med), 2)