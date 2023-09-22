def melhor_volta(matriz):
    tempo=[]
    i=0
    for linha in matriz:
        for a in linha:
            list.append(tempo,a)
    while min(tempo) not in matriz[i]:
        i+=1
    jogador=i+1
    volta=list.index(matriz[i],min(tempo))+1
    return (jogador,min(tempo),volta)