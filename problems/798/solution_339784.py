def freq_palavras(frases):
    texto = frases.splint()
    frequencia = []
    for palavra in texto:
        frequencia.append(texto.count(palavra))
    contador = {}
    for quantidade in range(len(texto)):
        contador[texto[quantidade]] = frequencia[quantidade]
    return contador