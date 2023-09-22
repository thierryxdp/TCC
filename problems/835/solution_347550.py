def melhor_volta(matriz):
    """Função que recebe uma matriz 6x10 com os tempos dos corredores em
       cada volta, retornando depois uma tupla com as informações de quem
       foi a melhor prova, com qual tempo e em que volta.
       
       Parameters: 
       matriz: Matriz com as informações dos corredores
       
       Returns: 
       Retorna uma tupla com as informações de quem foi a melhor prova,
       com qual tempo e em que volta.
       list -> tuple"""
    lista = []
    for i in range(1,7):
        list.append(lista,min(matriz[i-1]))
    tempo_min=min(lista)
    voltas=list.index(lista,tempo_min)+1
    numero_voltas=list.index(matriz[voltas-1],tempo_min)+1
    return (voltas,tempo_min,numero_voltas)