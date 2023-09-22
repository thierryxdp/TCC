def media_matriz(m):
    '''Função que dada uma matriz retorna a média de todos os números
    da matriz. list -> float'''
    elementos = 0
    soma = 0
    for i in range(len(m)):
        elementos += sum(m[i])
        soma = soma + i
    return round(elementos/soma, 2)