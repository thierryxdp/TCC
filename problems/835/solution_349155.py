def melhor_volta(lista):
    mv=100
    qt=100
    qv=100
    for i in lista:
        if min(i) < mv:
            qt=min(i)
            mv=i
            qv= list.index(i,min(i))
    return (mv,qt,qv)