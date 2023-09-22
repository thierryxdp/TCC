def melhor_volta(matriz):
    '''função em que dada uma matriz 6 x 10 (em que 6 são o número de corredores
    e 10 é o tempo em segundos que cada  corredor leva para dar cada uma das 10
    voltas). Retorne uma tupla informando: de quem foi a melhor volta da prova,
    com qual tempo e em que volta;
    list -> tuple'''
    t=0
    l=[]
    for i in range(6,0):
        l+=min(matriz[i])
    t=min(l)
    v=list.index(l,t)+1
    p=list.index(matriz[v-1],t)+1
    return (p,t,v)