def freq_palavras(s):
    '''Funcao que recebe uma string e retorna um dicionario onde as letras
    recebem a quantidade de vezes nas quais elas foram mencionadas
    str -> dict
    '''
    r= dict()
    s = list(s)
    for x in range(len(s)):
        r[s[x]] = s.count(s[x])
    return r