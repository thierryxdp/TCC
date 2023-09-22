def melhor_volta(lista):
    """Função que dada uma lista matrix retorna o qual a linha possui o menor valor, qual é e e qual a coluna;
    list->tuple"""
    mv=150
    qt=150
    qv=150
    for i in lista:
        if min(i) < qt:
            qt=min(i)
            mv=list.index(lista,i)+1
            qv= list.index(i,min(i))+1
    return (mv,qt,qv)