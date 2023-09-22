from collections import Counter

def repetidos(num):
    c = Counter(num)
    for numero, repeticoes in c.items():
        if repeticoes > 1:
            result = [indice for indice, item in enumerate(num) if item == numero]
            x = sum(result)
            return x