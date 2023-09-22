def buscaSetor(setor, P):
    '''Calcula e retorna os dados de um funcionario de
    determinado setor'''
    '''Str, list -> list'''
    lista_retorno = []
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno