def primo(num):
    """
    Função que dado um número inteiro positivo, verifica se esse número é primo ou não
    int-> bool
    """
    divisor = int(num/2)
    resposta = True
    if num!=0 and num!=1:
        while resposta and divisor > 1:
            if  num%divisor == 0:
                resposta = False
            divisor = divisor -1
        return resposta
    else:
        return False