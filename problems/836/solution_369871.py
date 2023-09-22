def busca(s,d):
    '''função que recebe uma matriz d com os dados dos funcionários
    de uma empresa e realiza uma busca pelas informações por setor s
    list -> list'''
    retorno = []
    for i in range(len(d)):
        if d[i][2] == s:
            list.remove(d[i],d[i][2])
            list.append(retorno,d[i])
    return retorno