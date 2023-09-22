def busca(setor, matriz):

#retorna uma matriz com os dados de pessoas de acordo com o setor
# str, matriz
    
    lista = []

    for l in range(0,3):
        if setor in matriz[l]:
            del matriz[l][2]
            lista.append(matriz[l])

    return lista