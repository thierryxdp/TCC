def melhor_volta(matriz:list)->tuple:
    '''Função que recebe uma matriz com os tempos em segundos dos 6 corredores de Kart em cada volta, e retorna uma tupla, informando de quem foi a melhor volta da prova, com qual tempo e em que volta.'''
    lista=[]
    lista_resultado=[0,0,0]
    for i in range(len(matriz_tempos)):
        for j in range(len(matriz_tempos[0])):
            list.append(lista,matriz_tempos[i][j])
    minimo=min(lista)
    for i in range(len(matriz_tempos)):
        for j in range(len(matriz_tempos[0])):
            if matriz_tempos[i][j]==minimo:
                lista_resultado[0]=i+1
                lista_resultado[1]=matriz_tempos[i][j]
                lista_resultado[2]=j+1
        
    return lista_resultado