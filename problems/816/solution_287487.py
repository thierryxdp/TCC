def maiores(lista[int],numero:int):
    """retorna os valores maiores que n em forma de lista"""
lista_final = []

for elemento in lista:
    if elemento > numero:
        lista_final.append(elemento)