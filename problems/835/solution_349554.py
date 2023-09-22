def melhor_volta(matriz):
    """Função que recebe uma matriz e retorna uma tupla informando de quem
    foi a melhor volta da prova com qual tempo e em que volta,lista-->tupla"""
    x=[0,0,0]
    lista_x= []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista_t,matriz[i][j])
    m= min(lista_x)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i][j]==m:
                x[0]=i+1
                x[1]=matriz[i][j]
                x[2]=j+1
    return tuple(x)