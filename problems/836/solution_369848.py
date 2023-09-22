def busca(setor, matriz):
    '''
    Função que recebe um setor e uma matriz de funcionários
    e retorna os dados dos funcionários daquele setor.
    
    str, list -> list
    '''
    func = []
    for funcionario in matriz:
        if setor == funcionario[2]:
            encontrado = funcionario[:]
            del encontrado[2]
            func.append(encontrado)
    return func