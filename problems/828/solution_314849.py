def primo(numero):
    resposta = False 
    for i in list(range(2,numero)):
        if numero%i==0:
             resposta = True
    return resposta