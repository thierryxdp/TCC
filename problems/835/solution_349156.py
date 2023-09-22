def melhor_volta(lista):
    mv=30
    qt=30
    qv=30
    for i in lista:
        if min(i) < mv:
            qt=min(i)
            mv=i
            qv= list.index(i,min(i))
    return (mv,qt,qv)