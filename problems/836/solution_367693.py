def busca(nome,matriz):
    """Dada um nome de setor e uma matriz com
    as informações dos funcionários da empresa
    retorna as informações daquele funcionário
    daquele setor correspondente ."""
    indice = 0
    listaVazia = []
    indiceSub = 0
    while indice < len(matriz):
        [matriz]
        if nome.title() in matriz[indice][indiceSub].title():
            listaVazia.append(matriz[indice])
        indice = indice + 1
    return listaVazia