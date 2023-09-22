def busca(setor,matriz):
    '''função que recebe uma matriz e faz uma busca em um setor e retorna uma sublista com os dados dos funcionarios que trabalham neste setor. str, list -> list'''
    resp = []
    for i in range (len(matriz)):
        if setor in matriz [i]:
            matriz[i].pop(2)
            resp.append(matriz[i])
    return resp