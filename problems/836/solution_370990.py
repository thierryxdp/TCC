def busca(setor:str,m:list)->list:
    '''Função que busca na matriz, com informações dos funcionários, quais pertencem ao setor solicitado.'''
    matriz=[]
    for i in range(len(m)):
            if setor in m[i]:
                matriz.append(m[i][2:]+m+[1[3:]])
    return matriz