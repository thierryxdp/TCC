def busca(setor, matriz):
    '''Dado o setor e uma matriz, retorna quais funcionarios trabalham naquele setor.
    str -> list'''
    func = []

    for i in matriz:
        if i[2] == setor:
            func.append(i)
    return func