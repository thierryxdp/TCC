def busca(setor, dados):
    '''funcao que, dado um setor e os dados dos funcionarios de uma empresa,
    retorna uma lista com os dados de todos os funcionarios daquele setor;
    str,matriz -> list(str,str,str)'''
    registros=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            info=[dados[i][0],dados[i][1],dados[i][3]]
            list.append(registros,info)
    return registros