def busca ( m: list, s: str)-> list:
    '''Retorna uma lista contendo os dados de todos os funcionários do
    setor s, dada uma matriz com os dados dos funcionários de uma empresa
    e o setor s'''
    lista = []
    for elem in m:
        if elem[2] == s:
            lista=lista.append(elem[:2] + elem[3:])
    return lista