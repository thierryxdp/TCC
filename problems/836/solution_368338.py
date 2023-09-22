def busca(setor, matriz):
    '''Retorna uma lista contendo os dados de todos os funcionarios que trabalham no setor procurado'''
    #str, list -> list
    lista = []
    posicao = 0
    for linha in matriz:
        
        for Aij in linha:
            if Aij == setor:
                list.append(lista, Aij)
                del lista[posicao][2]
                posicao = posicao + 1
                
    return lista