def pontos_por_time(lista1,lista2):
    l1=lista1
    l2=lista2
    x1=lista1[0]
    x2=lista1[1]
    l12=lista1[2]
    x3=l12[0]
    x4=l12[1]
    y1=lista2[0]
    y1=lista2[1]
    l22=lista2[2]
    y3=l22[0]
    y4=l22[1]
    dicionario=dict()
    if x3>x4 and y3>y4:
        dicionario[x1]='6 pontos'
        dicionario[x2]='0 pontos'
        return dicionario
    elif x3>x4 and y3=y4:
        dicionario[x1]='4 pontos'
        dicionario[x2]='1 ponto'
        return dicionario
    elif x3=x4 and y3>y4:
        dicionario[x1]='4 pontos'
        dicionario[x2]='1 ponto'
        return dicionario
    elif x3<x4 and y3<y4:
        dicionario[x2]='6 pontos'
        dicionario[x1]='0 pontos'
        return dicionario
     
    elif x3=x4 and y3<y4:
        dicionario[x2]='4 pontos'
        dicionario[x1]='1 ponto'
        return dicionario
    
    elif x3<x4 and y3=y4:
        dicionario[x2]='4 pontos'
        dicionario[x1]='1 ponto'
        return dicionario
    else:
        return dicionario