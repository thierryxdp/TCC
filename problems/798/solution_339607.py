def freq_palavras(frase):
    frequencia = {}
    for item in counter.items():
        frequencia[item[0]] = {'Total':item[1], 'Media': round(item[1]/3,2)}