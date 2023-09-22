def posLetra(frase, letra, numero):
    i = 0
    conta = 0
    frase_alterada = list()
    if numero > str.count(frase, letra):
        return -1
    while ( i < len(frase) and conta < numero):
        if letra in frase[i]:
            conta += 1
            list.append(frase_alterada, frase[i])
        else:
            list.append(frase_alterada, frase[i])
        i += 1
        return len(frase_alterada)