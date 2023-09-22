def melhor_volta(lista):
    mv=150
    qt=150
    qv=150
    for i in lista:
        if min(i) < qt:
            qt=min(i)
            mv=list.index(lista,i)+1
            qv= list.index(i,min(i))+1
    return (mv,qt,qv)