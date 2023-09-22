def busca(matriz,funcao):
    ''' funcao que dada uma matriz com os dados de funcionarios e uma funcao na empresa, retorna todos os empregados, e os seus dados, que excercem essa funcao. list,str --> list'''
    nova_lista = []
    for funcionarios in matriz:
        if funcionarios[2] == funcao:
            nova_lista.append(funcionarios[0:2])
            nova_lista.append(funcionarios[:3])
    return nova_lista