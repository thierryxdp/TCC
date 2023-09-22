def melhor_volta(matriz):
    menort=volta=vencedor=1000
    for v in range(0,len(matriz)):
        for t in range(0,len(matriz[v])):
            if min(matriz[v][t],menort)==matriz[v][t]:
                menort=min(matriz[v][t],menort)
                vencedor=v+1
                volta=t+1
    return vencedor,menort,volta