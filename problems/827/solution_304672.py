def qtd_divisores(n):
    "Conta quantos divisores um número tem. int->int"
    quant = 0
    for i in range(1,n+1):
        if (n%i==0):
            quant += 1
    return quant