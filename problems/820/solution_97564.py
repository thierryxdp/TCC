def posLetra(frase, letra, numero):
    i = 0
    conta = 0
    if numero > str.count(frase, letra):
        return -1
    frase_alterada = list()
    while ( i < len(frase) and conta < numero):
        if letra in frase[i]:
            conta += 1
        i += 1
        return len(frase[i])