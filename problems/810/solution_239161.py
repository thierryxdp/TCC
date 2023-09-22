def inverte(frase):
    """ Função que inverte a ordem das palavras de uma frase, tirando a pontuação e com todas as letras minusculas
    string --> string"""
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '/', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, '-', ' ')
    separar = str.split(frase)
    inverter = separar[::-1]
    juntar = str.join(" ", inverter)
    minuscula = str.lower(juntar)
    return minuscula