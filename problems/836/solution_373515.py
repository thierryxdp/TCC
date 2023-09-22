def busca ( m: list, setor: str)-> list:
    '''Retorna uma lista contendo os dados de todos os funcionários do
    setor s, dada uma matriz com os dados dos funcionários de uma empresa
    e o setor s'''
    lista = []
    for x in m:
        if setor in x[2] :
            lista=lista.append(x[:2] + x[3:])
    return lista