def busca(nome,matriz):
    """Dada um nome de setor e uma matriz com
    as informações dos funcionários da empresa
    retorna as informações daquele funcionário
    daquele setor correspondente ."""
    indice = 0
    listaVazia = []
    while indice < len(matriz):
        [matriz]
        if nome == matriz[indice][2]:
            listaVazia.remove(matriz[indice][2])
            listaVazia.append(matriz[indice])
        indice = indice + 1
    return listaVazia