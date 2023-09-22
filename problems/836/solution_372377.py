def busca(setor, dados):
    '''funcao que, dado um setor e os dados dos funcionarios de uma empresa,
    retorna uma lista com os dados de todos os funcionarios daquele setor;
    str,matriz -> list(str,str,str)'''
    registros=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            list.append(registros,dados[i])
            list.remove(registros,setor)
    return registros