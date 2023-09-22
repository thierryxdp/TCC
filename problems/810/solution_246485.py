def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return str(frases[-1:]) + str(frases[-2:-1]) + str(frases[-3:-2])