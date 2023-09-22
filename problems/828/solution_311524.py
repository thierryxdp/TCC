def primo(n):
    """
    Função que dado um número inteiro positivo, verifica se esse número é primo ou não
    int-> bool
    """
    divisor = int(n/2)
    resposta = True
    if n!=0 and n!=1:
        while resposta and divisor > 1:
            if  n%divisor == 0:
                resposta = False
            divisor = divisor -1
        return resposta
    else:
        return False