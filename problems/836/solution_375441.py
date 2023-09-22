def busca(setor,matriz):
    'função que recebe lista de funcionários, contendo nome, registro, setor'
    'e telefone e retorna todos os funcionários do setor solicitado.list->list'
    busca=[]
    i=0
    while i<len(matriz):
        if setor in (matriz[i][2]):
            del (matriz[i][2])
            busca.append(matriz[i])
        i+=1
    return busca