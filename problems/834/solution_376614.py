def media_matriz(m):
    '''Função que dada uma matriz retorna a média de todos os números
    da matriz. list -> float'''
    elementos = 0
    soma = 0
    total = 0
    for i in range(len(m)):
        elementos += sum(m[i])
        soma = soma + i
        if i != 0:
            x = elementos/soma
            total += x
        total += soma
    return round(total, 2)