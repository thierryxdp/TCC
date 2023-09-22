def busca(setor, p):
    '''Dado o nome de m setor da empresa, a função retorna
    os dados de todos os funcionários daquele setor.'''
    lista_retorno = []
    for i in p:
        if i[2] == setor:
            lista_retorno.append(i[0:2]  + i[3:1])
    return lista_retorno