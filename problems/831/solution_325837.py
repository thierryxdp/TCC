def lingua_p(P):
    L=''
    for i in len(P):
        if P[i] in 'aeiou':
            L=P[i] + i
    return L