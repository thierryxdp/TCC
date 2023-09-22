def uppCons(frase):
    """ a função transforma todas as consoantes no alfabeto
em maiscúlas, o metódo utilizado é de acumulação de retorno em outra string"""
    s = ''
    for consoante in frase:
        if consoante in 'bcçdfghjklmnpqrstvxwyz':
            s += consoante.upper()
        else:
            s += consoante
    return s