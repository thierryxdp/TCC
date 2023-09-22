def qtd_divisores(x):
    listax=[x]
    for i in range(1,x):
        if x<0:
            return 0
        elif x%i==0:
            list.append(listax,i)
    return len(listax)