def melhor_volta(m):
    '''função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla com de quem foi a melhor volta, com qual tempo e em que volta.
    list -> tuple'''
    lista=[]
    for c in m:
        t=min(c)
        list.append(lista,t)
    
    T=min(lista)
    C=1+list.index(lista,T)
    volta=0
    
    for c in m:
        i=0
        for tempos in c:
            if T==tempos:
                volta=i
            i=i+1
            
    return (C,T,volta+1)