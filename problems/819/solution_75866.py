def filtraMultiplos (l, n):
    'dada uma lista e um número "n", retorna os elementos da lista originais que sao multiplos de n. tr, int -> str'
    multiplos = []
    contador = 0
    while contador < len(l):
        if l[contador]%n == 0:
            multiplos = multiplos + [l[contador],]
        contador += 1
    return multiplos