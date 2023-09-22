def busca(setor, m):
    ''' Essa função retorna os dados de todos os funcionários de um determinado setor;
    str,list -> list. '''
    dados = []
    for i in range(0,len(m)):
        if setor in m[i]:
            del m[i][2]
            dados += [m[i]]
    return dados