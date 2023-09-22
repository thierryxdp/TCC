def busca(matriz,funcao):
    ''' funcao que dada uma matriz com os dados de funcionarios e uma funcao na empresa, retorna todos os empregados, e os seus dados, que excercem essa funcao. list,str --> list'''
    nova_lista = []
    for funcionarios in matriz:
        for dados in funcionarios:
            if dados == funcao:
            nova_lista += [funcionarios[0],funcionarios[1],funcionarios[3]]
    return nova_lista