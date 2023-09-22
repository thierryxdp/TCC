def melhor_volta(lista):
    mv=0
    qt=0
    qv=0
    for i in lista:
        for j in i:
            if min(j)<mv:
                qt=min(j)
                mv=i
                qv= list.index(j,min(j))
    return (mv,qt,qv)