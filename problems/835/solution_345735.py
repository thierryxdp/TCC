def melhor_volta (matriz):
    """Função que recebe uma matriz 6x10 e retorna o participante que fez a volta
    em menor tempo, o tempo que levou e qual foi a volta."""
    """list-->tuple"""
    tempos_total=[]
    ind=0
    for i in matriz:
        for j in matriz[ind]:
            tempos_total+=[j]
        ind+=1
    linha=0
    ind=0
    for i in matriz:
        linha+=1
        volta=0
        for j in matriz[ind]:
            volta+=1
            menor=min(tempos_total)
            if j==menor:
                resultado=(linha, j,volta)
        ind+=1
    return resultado