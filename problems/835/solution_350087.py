def melhor_volta(matriz):
    '''Dado os tempos dos corredores em matriz,
    a função mostrará quem teve a volta mais rápida
    o tempo de volta e qual foi essa volta.
    list->tupla'''
    menor=[]
    for i in matriz:
        menor=menor+[min(i)]
    menor_tempo=min(menor)
    piloto=list.index(menor,menor_tempo)
    volta=list.index(matriz[piloto],menor_tempo)   
    c=(piloto+1,menor_tempo,volta+1)
    return c