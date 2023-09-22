def primo(n:int)-> bool:
    resposta = True
    for i in range(2, n):
        if (n%i == 0):
            resposta = False
    return resposta