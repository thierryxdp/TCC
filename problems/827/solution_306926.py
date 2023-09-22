def qtd_divisores(x):
    listax=[x]
    for i in range(1,x):
        x=abs(x)
        if x%i==0:
            list.append(listax,i)
    return len(listax)