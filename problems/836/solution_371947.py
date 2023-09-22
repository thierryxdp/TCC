def busca (setor, funcionarios):
    '''Dada uma matriz (com o nome de um setor da empresa),
       retorne os dados de todos os funcionários do determinado
       setor;
       list, string -> list'''
    lista = []
    for i in range(len(funcionarios)):
        if setor in funcionarios[i]:
            aux = [funcionarios[i][0], funcionarios[i][1], funcionarios[i][3]]
            list.append(lista, aux)
    return lista