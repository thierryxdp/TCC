def pontos_por_time(lista1,lista2):
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
    pvt='6 pontos'
    pdt='0 pontos'
    pvp='4 pontos'
    pdp='1 pontos'
    dicionario=dict()
    if x3>x4 and y3>y4:
        dicionario[x1]=[pvt]
        dicionario[x2]=[pdt]
    
    if x3=x4 and y3=y4:
        dicionario[x1]=[pvp]
        dicionario[x2]=[pdp]
    
     if x3>x4 and y3=y4:
        dicionario[x1]=[pvp]
        dicionario[x2]=[pdp]
    
     if x4>x3 and y4>y3:
        dicionario[x2]=[pvt]
        dicionario[x1]=[pdt]
    
     if x4=x3 and y4>y3:
        dicionario[x2]=[pvp]
        dicionario[x1]=[pdp]
    
     if x4>x3 and y4=y3:
        dicionario[x2]=[pvp]
        dicionario[x1]=[pdp]
        
    return dicionario