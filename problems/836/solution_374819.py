def busca(setor, matriz):
    lista = []
    for funcionario in matriz:
        if (matriz[funcionario][2] == setor):
            lista.append(funcionario)
    return lista