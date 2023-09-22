def busca(pesquisa,matriz):
    for i in matriz:
        if pesquisa in matriz[i]:
            matriz[i].remove(pesquisa)
            result=matriz[i]
    return result