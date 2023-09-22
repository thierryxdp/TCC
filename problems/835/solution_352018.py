def melhor_volta(matriz):
    """Dada uma matriz 6x10 com os tempos dos corredores
    em cada volta retorna uma tupla com a pessoa, tempo 
    e volta da melhor volta da prova
    list -> tuple"""
    lista=[]
    for i in range(len(matriz)):
        minimo = min(matriz[i])
        lista.append(minimo)
        minimo = min(lista)
    for j in range(len(matriz)):
        for k in range(len(matriz[0])):
            if minimo == matriz[j][k]:
                pessoa = j+1
                tempo = matriz[j][k]
                volta = matriz[j].index(matriz[j][k])+1               
    return (pessoa,tempo,volta)