def carros(pessoas,capacidade=5):
    numero = pessoas//capacidade
    if numero > 0:
        numero += 1
    else:
        numero = numero
    return numero