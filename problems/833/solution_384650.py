from itertools import chain
from collections import Counter
def conta_ numero(numero,matriz):
	contador = Counter(chain.from_iterable(matriz))
	return (contador)