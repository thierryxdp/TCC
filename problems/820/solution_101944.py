def posLetra(string, letra, numero):
    if letra in string:
        return str.count(string, letra, numero)
    if letra not in string:
        return -1