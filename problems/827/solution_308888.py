def qtd_divisores(x):
    resultado=0
    for z in range(1,x+1):
        divisao=x%z
        if divisao==0:
            divisor=z
            resultado=resultado,z
    return resultado.count(resultado)