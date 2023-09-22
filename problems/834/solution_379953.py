def media_matriz(mat):
    '''função que dada uma matriz de números inteiros não vazia, retorna a média de todos os números da matriz com duas casas decimais de precisão; list (mat) -> float'''
    tam=(len(mat)*(len(mat[0])))
    total=0
    for i in mat:
        for j in i:
            total+=j
    med=total/tam
    return round(med,2)