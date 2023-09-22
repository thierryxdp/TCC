def soma_h(x):
#Dado o valor inteiro n, e feita a soma de n termos, int -> float
    soma = ()
    for n in range(1, x + 1):
        soma = soma + (1/n, )
    res = sum(soma)
    return round(res, 2)