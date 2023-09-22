from itertools import chain
from collections import Counter
def conta_numero(numero,matriz):
	contador = Counter(chain.from_iterable(matriz))
	return (contador)