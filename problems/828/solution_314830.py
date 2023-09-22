def primo(numero):
    
    qnt_div = 0
    for i in range(numero):
        if i>=2 and numero%i==0:
            qnt_div = qnt_div + 1
        elif i>=2 and numero%i!=0:
            qnt_div = qnt_div
    return qnt_div < 0