def conta_numero(numero,matriz):
   	"""Esta função recebe um numero inteiro e uma matriz de inteiros e conta
    quantas vezes o tal numero aparece na matriz."""
    for linha in matriz:
        numero = numero + list.count(linha,numero)
    return numero