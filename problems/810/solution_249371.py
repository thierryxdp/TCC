def inverte(frase):
    caract = ['-', ',', ':', ';', '.', '?', '!']
    for i in caract:
      frase = frase.replace(i, ' ')

    frase = frase.lower().split()
    return ' '.join(frase[::-1])