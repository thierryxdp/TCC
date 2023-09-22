def primo(numero):
    
    qnt_div = 0
    for i in range(numero):
        if i>=2 and numero%i==0:
            qnt_div = qnt_div + 1
        elif qnt_div > 0 :
            resposta = False
        elif qnt_div < 0 :
            resposta = True
    return resposta