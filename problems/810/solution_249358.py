def inverte(frase):
    caract = ['-', ',', ':', ';', '.', '?', '!']
    for i in caract:
      frase = frase.replace(i, ' ')
    return frase[::-1]