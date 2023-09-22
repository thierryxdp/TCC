def qtd_divisores(numero: int)-> int:
    """Dado um número, retorna quantos divisores esse número tem."""
    divisores = 0
    for candidato  in range(1,numero + 1):
        if (numero % candidato == 0):
            divisores += 1
    return divisores

def primo(numero: int)-> bool:
    """ Dado um número inteiro, retorna se esse número é
    primo ou não."""
    if (qtd_divisores(numero) == 2):
        return True
    else:
        return False