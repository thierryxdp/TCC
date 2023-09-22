def melhor_volta(matriz):
    pb=[]
    for linha in matriz:
        pb+=[min(linha)]
    a=min(pb)
    b=list.index(pb,a)
    c=list.index(matriz[b],a)
    return (b+1,a,c+1)