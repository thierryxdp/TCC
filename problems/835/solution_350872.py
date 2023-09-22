def melhor_volta(matriz:list)->tuple:
    '''diz a melhor volta: de quem foi, qual o número da volta e o tempo da volta'''
    melhor=0
    tempo=10000
    corredor=0
    indice=1
    for i in matriz:
        if min(i)<tempo:
            tempo=min(i)
            melhor=i.index(tempo)+1
            corredor=indice
        indice+=1
    return (corredor,tempo,melhor)