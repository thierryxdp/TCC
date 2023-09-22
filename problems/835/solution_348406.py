def melhor_volta (x):
    n_linhas=len(x)
    n_cols=len(x[0])
    tupla=()
    for i in range(n_linhas):
        for j in range(n_cols):
            for elementos in x:
        		a=min(elemento)
                tupla.append(i,j,a)
    return tupla