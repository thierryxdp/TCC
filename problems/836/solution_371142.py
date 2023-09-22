def busca(nome,matriz):
    '''Dado um nome e uma matriz, faz uma busca no setor e retorna os dados de todos os funcionares daquele setor.
    str, list -> list'''
    novalis=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i]:
                list.remove(matriz[i],nome)
                list.append(novalis,matriz[i])
    return novalis