def melhor_volta(matriz):
    '''funcao que dado uma matriz retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta
    list->tupla'''
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    for i in range(linha):
        list.append(lista,min(matriz[i]))
    tempo = min(lista)
    pessoa = list.index(lista,tempo)+1
    volta = list.index(matriz[pessoa-1],tempo)+1
    return (pessoa, tempo, volta)