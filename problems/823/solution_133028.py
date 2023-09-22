def faltante(lista):
    " " "Dada uma lista com N-1 inteiros numerados de 1 a N e descobre qualnúmero inteiro deste intervalo está faltando; list, -> int " " "
    list.sort(lista)
    i = 0
    n = 1
    while i<len(lista):
        if lista[i] == n:
            n = n + 1
        i = i + 1
    return n