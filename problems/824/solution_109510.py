def uppCons(frase):
    Retorno = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            Retorno = Retorno + frase[contador].upper
        else:
            Retorno = Retorno + frase[contador]
        contador += 1
    return Retorno