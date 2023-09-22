def qtd_divisores(numero):
    qnt_div = 0
    for i in range(numero):
        if i!=0 and numero%i==0:
             qnt_div = qnt_div + 1
        if numero < 0:
            qnt_div = 0
    return  qnt_div