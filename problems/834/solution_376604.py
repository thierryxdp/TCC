def media_matriz(m):
    '''Função que dada uma amatriz retorna a média de todos os números
    da matriz. list -> float'''
    elementos = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            elementos += len(m[i])
    return round(elementos/len(m), 2)