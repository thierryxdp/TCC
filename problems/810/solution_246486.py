def inverte(frases):
    if ',' in frases and '.' in frases and '-' in frases:
     return str((frases[-1:])+(frases[-2:-1])+(frases[-3:-2]))