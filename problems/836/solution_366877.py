def busca(string,matriz):
    '''Dada uma string, retorne os dados de todos os funcionários daquele setor na matriz;
    str,list -> list'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if string==matriz[2][j]:
                return matriz[i]
            else:
                return [[]]