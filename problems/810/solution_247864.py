def inverte(frase):
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.split(frase, ' ')
    list.reverse(frase)
    frase = str.join(' ',frase)
    frase = str.split(frase)
    return frase