def repetidos(x):
    i=0
    novalista = []
    while i < len(x):
        if x[i] < x[-1] and  x[i]==x[i+1]:
            novalista = novalista + [x[i]]
            i=i+1
        elif x[i] < x[-1] and x[i] != x[i+1]:
            i=i+1
        elif x[i] == x[-1]:
            return len(novalista)