def qtd_divisores(n):
    divisores = 0
    for i in range(1, n+1):
        if n%i == 0:
            divisores+=1
    return divisores

# Primeiro, temos um loop que passa por todos os números, de 1 até n. Após isso,
# verifica-se se o resto da divisão de n por i é igual a 0, o que significaria que
# i é um divisor de n, logo, o número de divisores recebe um incremento.