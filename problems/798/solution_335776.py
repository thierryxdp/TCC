def freq_palavras(frases):
    quantas_vezes=''
    separado=frases.split()
    for palavra in separado:
        if palavra==palavra:
            quantas_vezes=quantas_vezes+palavra
    return quantas_vezes