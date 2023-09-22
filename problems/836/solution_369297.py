def busca(nome,matriz):
    '''Dado um nome e uma matriz, faz uma busca no setor e retorna os dados de todos os funcionares daquele setor.
    str, list -> list'''
    nomescomum=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i]:
                list.remove(matriz[i],nome)
                list.append(nomescomum,matriz[i])
    return nomescomum