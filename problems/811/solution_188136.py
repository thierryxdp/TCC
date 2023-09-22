# Retorna se o colchão passsa pela porta, passando as medidas do colchão e as medidas da porta
# array, int, int -> bool
def colchao(medidas, h, l):
    return medidas[1] <= h or medidas[1] <= l