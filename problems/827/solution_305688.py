def qtd_divisores(numero: int)-> int:
    """Dado um número, retorna quantos divisores esse número tem."""
    candidato_divisor = list(range(1,numero + 1))
    divisores = 0
    for (candidato  in candidato_divisor):
        if (numero % candidato == 0):
            divisores += 1
    return divisores