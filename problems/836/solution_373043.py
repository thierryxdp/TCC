def busca(setor,m):
    '''Recebe uma matriz que representa os funcionários da empresa e retorna uma lista com todos os funcionários do setor de entrada; list->list'''
    contador=0
    resposta=[]
    while contador<len(m):
        if m[contador][2]==setor:
            list.append(resposta,m[contador])
    	contador=contador+1
    return resposta