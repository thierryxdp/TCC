def melhor_volta(matriz):
    '''função que recebe como entrada uma matriz 6x10 onde as linhas 
    representam os corredores numerados de 1 a 6, e as colunas representam
    as voltas numeradas de 1 a 10, em que os elementos da matriz representam
    o tempo, em segundos, de cada volta de cada corredor; retorna uma tupla
    contendo quem obteve a melhor volta,o tempo desta volta, e qual foi a 
    numeração da volta deste corredor; list(list)->tuple(int,float,int)'''
    
    lista=[]
    
    for linha in matriz:
        melhor=min(linha)
        list.append(lista,melhor)
    
    tempo=min(lista)
    vencedor=list.index(lista,tempo)+1
    volta=list.index(matriz[vencedor-1],tempo)+1
    
    return (vencedor,tempo,volta)