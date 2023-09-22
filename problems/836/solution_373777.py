def busca(setor, matriz):
    lista = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            copia = list.copy(funcionario)
            list.remove(copia, setor)
            list.append(lista, copia)
    return lista