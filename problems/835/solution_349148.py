def menorn(matriz):
    menor = matriz[0][0]
    for r in range(len(matriz)):
        nums = matriz[r]
        for n in nums:
            menor = n if menor > n else menor
    return menor
def melhor_volta(matriz):
	result=[]
	tempo=menorn(matriz)
    quem=index(tempo)
    result.append(quem)
    result.append(tempo)
    return result