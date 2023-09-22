def busca(elemento,matriz):
    """Função que recebe uma matriz e faz uma busca por 
    setor. Ou seja, dado o nome de um setor da empresa, a 
    função retorna os dadosde todos os funcionários daquele
    setor.
    str,matriz->list"""
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if elemento in matriz[i][j]:
                lista.append(matriz[i])
    for k in lista:
        for o in k:
            if o==elemento:
                indice=k.index(elemento)
                del k[indice]
    return lista