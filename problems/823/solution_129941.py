def faltante(lista):
    """calculo e retorno de uma lista que venha com o numero faltando na lista original."""
    n = len(lista) + 1
    completa= n * (n + 1) // 2
    return completa - sum(lista)