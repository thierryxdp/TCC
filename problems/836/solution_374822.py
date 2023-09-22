def busca(setor, matriz):
    lista = []
    for funcionario in range(0,len(matriz)):
        if (matriz[funcionario][2] == setor):
            lista.append(funcionario)
    return lista