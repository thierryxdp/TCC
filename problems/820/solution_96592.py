def posLetra(frase,letra_desejada,ocorrencia_desejada):
    numero_de_vezes = 0
    numero_de_letras = 0
    if letra_desejada not in frase:
        return -1
    for letra in frase:
        if letra == letra_desejada:
            numero_de_vezes += 1
        numero_de_letras += 1
        if numero_de_vezes == ocorrencia_desejada:
            return numero_de_letras - 1