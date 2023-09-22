def melhor_volta(matriz):
    '''recebe uma matriz com o numero de voltas e o tempo
    de 6 corredores e retorna quem fez a melhor volta
    em quanto tempo e em qual volta
    
    entra: list
    sai:tupla'''
    
    lista=[]
    for i in matriz:
        for k in i:
            lista.append(k)
            melhor=min(lista)
            if melhor in i:
                tupla=(matriz.index(i)+1,melhor,i.index(melhor)+1)
    return tupla