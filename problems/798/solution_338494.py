def freq_palavras(frases):
    texto = frases.split()
    frequencia = []
    contador = {}
    for i in range(len(texto)):
        contador[texto[i]] = frequencia [i]
    return contador