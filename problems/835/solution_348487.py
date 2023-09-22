def melhor_volta(m):
    """funcao que dada uma matriz com os tempos de corredores returne uma tupla dizendo quem foi melhor.
    list-->tuple."""
    lista=[]
    x=0
    for i in range(len(m)):
        x=min(m[i])
        lista.append(x)
    x=min(lista)
    p=lista.index(x)
    t=list.index(m[3],x)
    return (p+1,x,t+1)