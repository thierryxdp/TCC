def busca(setor,matriz):
    '''Ao fornecer uma matriz com as listas referentes aos dados dos
    funcionários e um determinado setor, verifica quais desses funcionários
    pertence a este setor. Caso alguém pertença ao setor, retorna a lista com os dados desse funcionário, caso negativo, retorna
    uma lista vazia.

    str, list -> list'''
    
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (setor in matriz[i][2]) and (matriz[i] not in dados):
                list.append(dados,matriz[i])
                list.remove(matriz[i],matriz[i][2])

    return dados