def busca(setor, matriz):
    '''Dado o setor e uma matriz, retorna quais funcionarios trabalham naquele setor.
    str -> list'''
    func = []

    for i in matriz:
        aux = []
        if i[2] == setor:
            aux.append(i[0])
            aux.append(i[1])
            aux.append(i[3])
            func.append(aux)
    return func