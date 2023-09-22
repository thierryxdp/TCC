def melhor_volta(matriz6x10):
    """Função que dada uma matriz 6x10 contendo o tempo em  segundos dos
       corredores em cada volta retorna uma tupla informando de quem foi 
       o melhor tempo de prova, e qual é esse tempo, em qual volta.
       
       Parameters:
       matriz6x10: é a matriz que contém as informações dos tempos de cada
       corredor em cada volta
       
       Returns:
       Retorna uma tupla com as informações de quem teve o melhor tempo e 
       em qual volta.
       list -> tuple
       """
    lista = []
    for i in range(1,7):
        list.append(lista,min(matriz6x10[i]))
    tempo_min = min(lista)
    volta = list.index(lista, tempo_min)+1
    numero_voltas = list.index(matriz6x10[volta-1], tempo_min)+1
    return (volta,tempo_min,volta)