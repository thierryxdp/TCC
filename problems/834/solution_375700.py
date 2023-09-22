def media_matriz(m):
    "Função média calcula a média de todos os números de uma matriz"
    acumulador = 0
    count = 0
    for i in m:
        count += len(i)
        for j in i:
            acumulador += j
    return (type(round(acumulador/count,2)))