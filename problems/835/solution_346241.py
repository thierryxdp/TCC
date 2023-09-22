def melhor_volta(matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    for i in range(linha):
        list.append(lista,min(matriz[i]))
    tempo = min(lista)
    pessoa = list.index(lista,tempo)+1
    volta = list.index(matriz[pessoa-1],tempo)+1
    return (pessoa, tempo, volta)