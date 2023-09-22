def qtd_divisores(n):
    """Conta o número total de divisores de um número inteiro n.
Teses: qtd_divisores(10) == 4
qtd_divisores(7) == 2
assinatura: int --> int
"""
    divisores = 1
    contagem = 0
    while divisores <= n:
        if n%divisores == 0:
            contagem = contagem + 1
            divisores = divisores + 1
        else:
            divisores = divisores + 1
    return contagem

def primo(n):
    """Recebe um número inteiro positivo n e retorna true caso n for um número primo.
testes: primo(2) == True
primo(4) == False
assinatura: int --> bool
"""
    if qtd_divisores(n) <= 2:
        return True
    else:
        return False