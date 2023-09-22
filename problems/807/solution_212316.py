def conta_frases (frases):
    texto = frases.split('...')
    quant_frases = len(texto) - 1
    for h in range(0, len(texto), 2):
        for i in list(texto[h]):
            if i == '!' or i == '?' or i == '.':
                quant_frases += 1
    return quant_frasesS