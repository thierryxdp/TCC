def qtd_divisores(n):
    soma = 0
    for c in range(1,n):
        if n //c ==0:
            soma+=1
    return soma