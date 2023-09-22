def uppCons(frase):
    """ Função que, dados uma frase, retorna a frase com suas consoantes
    em maiúsculas.
    str -> str"""

    i = 0


    while i < len(frase):

        if frase[i] in 'bcnmqwrtypsdfghjlçzxv':
            frase = frase.replace(frase[i], frase[i].upper())
        i=i + 1
    return frase