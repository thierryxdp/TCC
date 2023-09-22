from collections import defaultdict
def repetidos(num):
    c = Counter(num)

    for numero, repeticoes in c.items():
        if repeticoes > 1:
            result = [indice for indice, item in enumerate(lista) if item == numero]