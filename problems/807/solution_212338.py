def conta_frases (frases):
    '''Retorna a quantidade de frases inseridas "frases" após separar cada uma delas conforme os sinais de pontuação ".", "!", "?" e "...";
    str -> int'''
    texto = frases.split("...")
    quant_frases = len(texto) - 1
    for h in range(0, len(texto), 2):
        for i in list(texto[h]):
            if i == "!" or i == "?" or i == ".":
                quant_frases += 1
    return quant_frases