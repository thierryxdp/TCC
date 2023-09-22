def melhor_volta(matriz):
    '''funcao que recebe os tempos em segundos de corredores em cada volta 
    e retorna informando de quem foi a melhor volta, com qual tempo e em que volta
    float->tupla'''
    corredores=[]
    for j in range(len(matriz)):
        corredores=corredores+[min(matriz[j])]
        melhort=min(jogadores)
        melhorc=list.index(corredores,melhort)
        melhorv=list.index(matriz[melhorc],melhort)
        return (melhorc+1,melhort,melhorv+1)