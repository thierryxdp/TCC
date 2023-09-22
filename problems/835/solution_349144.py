def melhor_volta(matriz):
    resultado=[]
    tmepo= min(matriz)
    for i in tmepo:
        tempo=min(i)
        resultado.append(tempo)
    return tuple(resultado)