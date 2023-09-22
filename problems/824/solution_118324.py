def uppCons(f):
    """
  função que recebe uma frase e retorna a frase com todas as suas 
  consoantes em maiusculas, mantendo os demais caracteres
    :param frase: str
    :return: str
    """
    cont = 0
    frase = ''
    while cont < len(f):
        if f[cont] not in 'aeiouãéíóú':
            frase += f[cont].upper()
        else:
            frase += f[cont].lower()
        cont += 1

    return frase