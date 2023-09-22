def melhor_volta(lista):
    mv=0
    qt=0
    qv=0
    for i in lista:
        if min(i) < mv:
            qt=min(i)
            mv=i
            qv= list.index(i,min(i))
    return (mv,qt,qv)