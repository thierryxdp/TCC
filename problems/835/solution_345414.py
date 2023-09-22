def melhor_volta(matriz):
    """A função informa quem foi a melhor volta da prova, com qual tempo
       e em que volta;
       list->tuple
       Parâmetro:
       matriz: uma matriz 6x10
    """
    tempo=[]
    for i in range(len(matriz)):
        list.append(tempo,min(matriz[i]))
    menor=min(tempo)
        
    for i in range(len(matriz)):
        if menor in matriz[i]:
            corredor=i+1
        vezes=list.index(matriz[i],menor)+1
        
    return (corredor,menor,vezes)