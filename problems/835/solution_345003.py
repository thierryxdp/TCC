def melhor_volta(matriz):

    lista = []


    for l in range(0, 6):
        lista.append(min(matriz[l]))

    indice = lista.index(min(lista))
    linha = matriz[indice]

    return (lista.index(min(lista))+1, min(lista), linha.index(min(linha))+1)