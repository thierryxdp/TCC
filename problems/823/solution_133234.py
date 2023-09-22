def faltante (lista_p)
"""Função que retorna o numero de peças faltantes de um quebra-cabeça
list -> int"""
lista = []
x = 0
lista_p.sort()
while x < (len(lista_p)-1):
    if lista_p[x+1] - lista_p[x] > 1:
        return x + 2
    x = x + 1
if lista_p[0] == 1:
    return lista_p[-1]+1
else:
    return lista_p[0]-1