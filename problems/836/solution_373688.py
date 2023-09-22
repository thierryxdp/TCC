def busca(setor,matriz):
    '''Dada uma matriz com as informações de cada
    funcionário e o setor desejado, retorna todas
    as informações sobre os funcionários daquele
    setor.
    str, list -> list'''
    r = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            r += matriz[i]
        else:
            r += r        
    return r