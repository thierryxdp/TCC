def posLetra(string, letra, numero):
    " Função que retorna em que posição da string a ocorrência da leetra está."
    i=0
    contador=0
    while i < len(string)-1:
        if string[i] == letra:
            contador += 1
        if contador == numero:
            return i
        i += 1
    return -1