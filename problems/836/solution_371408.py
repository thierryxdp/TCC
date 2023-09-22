def busca(s,m):
    '''Retorna os dados de todos os funcionários contidos na matriz m do setor
       a ser identificado a partir da string s de entrada;
       str, list -> list'''
    lRetorno=[]
    for i in range(len(m)):
        if m[i][2]==s:
            dadosRetorno=m[i][:]
            dadosRetorno.remove(s)
            lRetorno.append(dadosRetorno)
    return lRetorno