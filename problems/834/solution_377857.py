def media_matriz(m):
    '''dada uma matriz de inteiros não vazia(m), retorna a média de todos
    os números da matriz(com duas casas decimais de precisão);;
    list -> float'''
    total = 0
    e = 0
    for i in m:
        total = total + sum(i)
        e = e + len(i)
    return round(total/e,2)