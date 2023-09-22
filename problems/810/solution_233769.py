def inverte(frase):
    frase=frase.replace('?', ' ')
    frase=frase.replace('!', ' ')
    frase=frase.replace('-', ' ')
    frase=frase.replace('.', ' ')
    frase=frase.replace(',', ' ')
    return str.join('',frase.split()[::-1])