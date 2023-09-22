def carros(pessoas,capacidade=5):
    numero = pessoas//5
    if numero > 0:
        numero += 1
    else:
        numero = numero
    return numero