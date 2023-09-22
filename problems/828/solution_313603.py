def primo(n:int)-> bool:
    resposta = False
    for i in range(3, n):
        if (n%i == 0):
            reposta = True
    return resposta