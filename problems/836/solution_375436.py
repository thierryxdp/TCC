def busca(setor,matriz):
    'função que recebe lista de funcionários, contendo nome, registro, setor'
    'e telefone e retorna todos os funcionários do setor solicitado.list->list'
    busca=[]
    for i in matriz:
        for j in matriz:
            if matriz[i][j]==setor:
                busca=busca+((matriz[i][j]),)
    return busca