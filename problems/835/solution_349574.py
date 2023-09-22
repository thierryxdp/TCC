def melhor_volta(m):
    '''dada uma matriz 6x10, retorna uma tupla informando
    de quem foia a melhor volta da prova, com qual tempo e em que volta
    list -> list'''
    
    lista=[0,0,0]
    listaT=[]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            list.append(listaT,m[i][j])
    minimo=min(listaT)
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==minimo:
                lista[0]=i+1
                lista[1]=m[i][j]
                lista[2]=j+1
                
    return tuple(lista)