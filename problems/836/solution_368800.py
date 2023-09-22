def busca(setor,matriz):
" " "Recebe uma matriz com informações de funcionarios e faz uma busca de funcionarios por setor;string, list, -> list " " "
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            del matriz[i][2]
            lista.append(matriz[i])
    return lista