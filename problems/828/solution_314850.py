def primo(numero):
    resposta = True 
    for i in list(range(2,numero)):
        if numero%i==0:
             resposta = False
    return resposta