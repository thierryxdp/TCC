def primo(n:int)-> bool:
    resposta = False
    for i in range(2, n):
        x=n%i
        if (x == 0):
            reposta = True
    return resposta