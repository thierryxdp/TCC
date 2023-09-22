def qtd_divisores(x):
    resultado=''
    for z in range(1,x+1):
        divisao=x%z
        if divisao==0:
            divisor=z
            resultado=resultado+','+str(z)
    return str.count(resultado,',')