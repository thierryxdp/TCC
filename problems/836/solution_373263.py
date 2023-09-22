def busca(area, matriz):
    '''Encontro um funcionário dado sua área na empresa.
str,list-list'''

    ret = []
    for l in range(0, len(matriz)):
        for c in range(0, len(matriz[l])):
            if area.lower() == matriz[l][c].lower():
                dados = matriz[l].copy()
                dados.pop(dados.index(dados[c]))
                ret.append(dados)

    return ret