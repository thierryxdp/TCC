def melhor_volta (matriz):
    """Função que, dado um número inteiro e uma matriz de inteiros qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz."""
    """int, list-->int"""
    tempos_total=[]
    ind=0
    for i in matriz:
        for j in matriz[ind]:
            tempos_total+=j
        ind+=1
    for i in matriz:
        for j in matriz[ind]:
            if j=min(tempos_total):
                resultado=(i+1, matriz[i][j],j+1)
                
    return resultado