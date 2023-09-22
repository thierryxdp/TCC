def inverte (frase):
    frase = str. replace(frase, '-', ' ')
    frase = str. replace(frase, ',', ' ')
    frase = str. replace(frase, ':', ' ')
    frase = str. replace(frase, ';', ' ')
    frase = str. replace(frase, '.', ' ')
    frase = str. replace(frase, '!', ' ')
    frase = str. replace(frase, '?', ' ')
    frase = str. replace(frase, '...', ' ')
    frase = [::-1]
    return frase