def busca(setor,matriz):
    """ Função que dada um setor da empresa, fornece os dados dos funcionarios do setor
    str,list -> list """
    lista=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            lista=lista+[[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return lista