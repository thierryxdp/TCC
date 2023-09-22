def busca(setor,matriz):
    '''Dada uma matriz com as informações de cada
    funcionário e o setor desejado, retorna todas
    as informações sobre os funcionários daquele
    setor.
    str, list -> list'''
    r = []
    for i in matriz:
        for j in i:
            if j == setor:
                r = [matriz[i].remove(setor)]
            else:
                r = []        
    return r