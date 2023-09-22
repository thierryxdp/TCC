def primo(n:int)-> bool:
    resposta = False
    for i in range(2, n-1):
        if (n%i == 0):
            reposta = True
    return resposta