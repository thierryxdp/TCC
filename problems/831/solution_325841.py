def lingua_p(P):
    L=''
    i=0
    for l in P:
        if P[i] in 'aeiou':
            L=P[i] + 'p'
    return L