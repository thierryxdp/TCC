#int->int
def qtd_divisores(num):
    #a função retorna a quantidade de divisores
    q_div=0
    while q_div<=num :
        if num % q_div == 0:
            q_div += 1
    #a quantidade de divisores até aqui, resulta um termo com uma inidade a menos
    if q_div > 0:
        q_div += 1
    # para isso, peguei a variável resultante e acrescentei uma unidade
    return q_div