def melhor_volta(m):
    """funcao que dada uma matriz com os tempos de corredores returne uma tupla dizendo quem foi melhor.
    list-->tuple."""
    lista=[]
    x=0
    for i in range(len(m)):
        x=min(m[i][o])
        lista.append(x)
        p=lista.index(x)
    return (m[p][0],x)