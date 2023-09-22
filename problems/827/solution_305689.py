def qtd_divisores(numero: int)-> int:
    """Dado um número, retorna quantos divisores esse número tem."""
    divisores = 0
    for candidato  in range(1,numero + 1):
        if (numero % candidato == 0):
            divisores += 1
    return divisores