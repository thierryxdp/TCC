def pontos_por_time(L):
    i=L[0]
    v=L[1]
    Pi=i[2]
    Pv=v[2]
    G1i=Pi[0]
    G2i=Pi[1]
    G1v=Pv[0]
    G2v=Pv[1]
    if G1i>G2i:
        T1i=3
        T2i=0
    elif G1i<G2i:
        T1i=0
        T2i=3
    else:
        T1i=1
        T2i=1
    if G1v>G2v:
        T1v=3
        T2v=0
    elif G1v<G2v:
        T1v=0
        T2v=3
    else:
        T1v=0
        T2v=0
    T1=T1i+T1v
    T2=T2i+T2v
    
    nome_pontuacao={i[0]:T1 ,i[1]:T2}
    return nome_pontuacao