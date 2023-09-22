def busca(setor,matriz):
    '''retorna os dados de todos os funcionarios pertinentes
    ao setor buscado
    str, list(list) -> list(list)'''
    y=[]
    for pes in range(len(matriz)):
        i=0
        for x in range(len(matriz[pes])):
            if setor == matriz[pes][i]:
                list.append(y,[matriz[pes][0],matriz[pes][1],matriz[pes][3]])
            i+=1
    return y