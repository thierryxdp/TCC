def melhor_volta(matriz):
    '''função que recebe como entrada uma matriz e retorna uma tupla; matriz->tuple'''
    listamin = []:
        for i in range (len(matriz)):
            listamin = listamin + [min(matriz[i])]
        tempo = min(listamin)
        quem_foi = list.index(listamin,tempo)
        volta = list.index(matriz[quem_foi],tempo)
        return (quem_foi + 1,tempo,volta + 1)