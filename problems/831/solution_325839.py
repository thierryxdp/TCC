def lingua_p(P):
    L=''
    for i in str(P):
        if P[i] in 'aeiou':
            L=P[i] + i
    return L