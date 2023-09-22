"""Recebe uma lista de medidas do colchão e dois inteiros indicando altura
e largura da porta e retorna se é possível passar o colchao pela porta
list, int, int-> boolean"""
def colchao(medidas, h, l):
    return medidas[1] <= h