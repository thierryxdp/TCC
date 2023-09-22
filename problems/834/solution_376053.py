def media_matriz(matriz):
    lista_medias = []
    for j in range(n):
        soma = 0
        for i in range(m):
            soma = soma + tabela_notas[i][j]
        media = soma / m
        lista_medias.append(media)

    return lista_medias