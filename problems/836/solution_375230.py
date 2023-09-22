def busca(setor,matriz):
    '''função em dada uma matriz, faça uma busca por setor e retorna os dados
    de todos os funcionários desse setor
    str, list -> tupla'''
    resultado=[]
    for linha in range(len(matriz)):
        if setor==matriz[linha][2]:
            list.remove(matriz[linha],setor)
            list.append(resultado,matriz[linha])
    return resultado