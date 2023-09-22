def busca(string,matriz):
    '''Dada uma string, retorne os dados de todos os funcionários daquele setor na matriz;
    str,list -> list'''
    matriz2=[]
    for dados in matriz:
        for setor in dados[2]:
            if string==setor:
                del(dados,setor)
                list.append(matriz2,dados)
                
    return matriz2