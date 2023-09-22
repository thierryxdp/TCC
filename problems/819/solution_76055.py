def filtraMultiplos (lista, n):
    elemento = lista[:]
    while elemento in lista % n != 0:
        return lista.pop(elemento)