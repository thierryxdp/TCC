def filtraMultiplos(n,lista):
    resultado = []
    i=0
    while i < len(lista):
        elemento = lista[i]
        if n%elemento == 0:
            resultado.append(elemento)
        i = i+l
        return resultado