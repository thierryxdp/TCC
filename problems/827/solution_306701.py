def qtd_divisores(numero):
    divisor=1
    resultado=[numero]
    if numero<0:
        return 0
    for n in range(numero):
        if n>0:
            if numero%n==0:
                resultado.append(n)
    return len(resultado)
'''dado um numero, a funcao retorna a quantidade de divisores
que esse numero tem
int->int'''