def qtd_divisores(x):
    listax=[x]
    for i in range(1,abs(x)):
        if x%i==0:
            list.append(listax,i)
    return len(listax)