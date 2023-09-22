def freq_palavras(frases):
    quantas_vezes=0
    separado=frases.split()
    for palavra in separado:
        if palavra==palavra:
            quantas_vezes= quantas_vezes + (palavra.count(palavra))
    return quantas_vezes