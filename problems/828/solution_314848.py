def primo(numero):
    resposta = 0 
    for i in list(range(2,numero)):
        if numero%i==0:
             resposta = True
        if numero%i!=0:
            resposta = False 
    return resposta