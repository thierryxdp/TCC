def posLetra (frase, letra, n):
    quantas = str.count(frase, letra)
    if n < quantas:
        return -1
    else:
        return str.find(frase, letra, n)