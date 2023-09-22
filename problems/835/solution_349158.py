def melhor_volta(lista):
    mv=150
    qt=150
    qv=150
    for i in lista:
        if min(i) < mv:
            qt=min(i)
            mv=list.index(lista,i)
            qv= list.index(i,min(i))+1
    return (mv,qt,qv)