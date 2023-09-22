def freq_palavras(frases):
    quantas_vezes={}
    separado=frases.split()
    for palavra in separado:
        quantas_vezes.update({palavra:separado.count(palavra)})
    return quantas_vezes