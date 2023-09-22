def qtd_divisores(numero):
    d=1
    res=[numero]
    for n in range(numero):
        if n!=0:
            if numero%n==0:
                res.append(n)
    return len(res)