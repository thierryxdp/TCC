def busca(s, m):
    '''
    Esta função recebe uma string com um setor e uma matriz onde cada linha contem o nome , registro, setor 
    e número de telefone de um funcionário.
    Retorna uma matriz contendo os dados de todos os funcionarios que trabalham no setor informado.
    Parametros
    ----------
    s (str) : setor
    m (list) : matriz
    '''
    l = [i for i in m if s in i]
    for c in l:
        c.pop(2)
    return l