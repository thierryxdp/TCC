def primo(n):
    """ Função que verifica se um número inteiro positivo é primo e
retorna um valor booleano
Assinatura: int--> bool
Testes:
primo(1) == True
"""
    i = 2
    while i < n:
        if (n%i == 0):
            return False
        i += 1
    return True