def qtd_divisores(n):
    lista = list(range(1,n))
    soma = 0
    for i in lista:
        if n%lista[i] == 0:
            soma = soma + 1
    return soma