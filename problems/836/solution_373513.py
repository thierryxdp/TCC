def busca ( m: list, setor: str)-> list:
    '''Retorna uma lista contendo os dados de todos os funcionários do
    setor s, dada uma matriz com os dados dos funcionários de uma empresa
    e o setor s'''
    lista = []
    for elem in m:
        if setor == elem[2] :
            lista=lista.append(elem[:2] + elem[3:])
    return lista