def busca(setor, dados):
    '''funcao que, dado um setor e os dados dos funcionarios de uma empresa,
    retorna uma lista com os dados de todos os funcionarios daquele setor;
    str,matriz -> list(str,str,str)'''
    registros=[]
    for setor in range(len(dados)):
        for info in dados[setor]:
            list.append(registros,info)
    return [registros[0:2]+ registros[3:]]