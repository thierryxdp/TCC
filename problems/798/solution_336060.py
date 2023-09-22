def freq_palavras(frases):
    quantas_vezes=0
    separado=frases.split()
    for palavra in separado:
           quantas_vezes= quantas_vezes + (separado.count(palavra))
    return quantas_vezes