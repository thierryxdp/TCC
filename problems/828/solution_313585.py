#Armazenarei os divisores de n numa lista
#
def primo(n):
    lista = []
    numero = list(range(n))
    for x in numero:
        if x >= 2 and n % x == 0:
            list.append(lista, x)
    return len(lista) == 0