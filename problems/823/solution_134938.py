def faltante(l):
    """Minha função, usa n como termo final ou seja ultima peça, depois disso
    eu uso a formula da PA para calcular a soma de todos os numeros entre 1 e N,
    depois disso usei a formula da PA e subtrai pelos elementos da lista com sum"""
    n = len(l) + 1
    somatotal = n * (n + 1) // 2
    return somatotal - sum(l)