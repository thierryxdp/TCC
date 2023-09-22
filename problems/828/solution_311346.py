def primo(n):
    resposta = 0
    for i in list(range(1,n+1)):
        if n%i == 0:
            resposta+=1
    return resposta == 1