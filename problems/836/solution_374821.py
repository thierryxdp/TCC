def busca(setor, matriz):
    lista = []
    for funcionario in range(0,matriz):
        if (matriz[funcionario][2] == setor):
            lista.append(matriz[funcionario])
    return lista