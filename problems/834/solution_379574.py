def media_matriz(m):
    cont = 0
    acum = 0

    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            acum += m[linha][coluna]
            cont += 1

    return round((acum/cont),2)