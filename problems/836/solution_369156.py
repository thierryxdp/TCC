def busca(setor,matriz):
    lista_nova = []
    for i in range(len(matriz)):
        if matriz[i][2] in setor:
            lista_nova.append(contatos[i])
    return lista_nova