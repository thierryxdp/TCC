def melhor_volta(matriz):
    '''Função que dada matriz fixada 6 por 10, retornará uma tupla contendo de qual corredor foi a melhor volta,qual tempo e qual volta; matriz>>tuple'''
    corredor= -1
    tempo= -1
    volta= -1
    s=[]
    for k in matriz:
        list.append(s, min(k))
        tempo= min(s)
        for j, k in enumerate(matriz,1):
            if tempo in k:
                corredor= j
                volta=list.index(k,tempo)+1
    return corredor,tempo,volta