def qtd_divisores(x):
    j=[]
    for e in range(x+1):
        if e != 0:
            if x%e==0:
                list.append(j,e)

    return len(j)