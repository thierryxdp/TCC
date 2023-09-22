def qtd_divisores(x):
    'retorna quantos divisores x tem'
    divisores = 0
    for numeros in range(1,x+1):
        if x%numeros == 0:
            divisores = divisores + 1
    return divisores