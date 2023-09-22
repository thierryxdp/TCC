def melhor_volta (x):
    n_linhas=len(x)
    n_cols=len(x[0])
    tupla=()
    for el in x:
        a=min(el)
        for i in range(el[a]):
            for j in range(a):
    tupla=((i),(a),(j))
    return tupla