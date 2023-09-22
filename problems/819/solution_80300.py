def filtraMultiplos(lista, n):
meus_numeros = [1, 56, 342, 12, 781, 23, 43, 45, 123, 567]
lista = []
for c in meus_numeros: 
    if c%n == 0: 
        lista.append(c)