def busca (s: str, m: list)-> list:
    '''Retorna uma lista contendo os dados de todos os funcionários do
    setor s, dada uma matriz com os dados dos funcionários de uma empresa
    e o setor s'''
    lista = []
    for i in range(len(m)):
        if s in m[i]:
            x = m[i]
            lista.append(x[:2] + x[3:])
    return lista