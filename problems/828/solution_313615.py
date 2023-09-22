def primo(n:int)-> bool:
    """Função que dado um número inteiro positivo verifica se esse número é primo ou não, caso seja, retorna True, caso contrário, retorna False."""
    resposta = True
    for i in range(2, n):
        if (n%i == 0):
            resposta = False
    return resposta