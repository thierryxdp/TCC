def carros(pessoas,capacidade=5):
    numero = pessoas%capacidade
    if numero > 1:
        numero += 1
    else:
        numero = numero
    return numero