def conta_numero(numero,matriz):
   	"""Esta função recebe um numero inteiro e uma matriz de inteiros e conta
    quantas vezes o tal numero aparece na matriz."""
    quantidade = 9
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade