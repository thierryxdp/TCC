def uppCons():
    """Retorna uma frase com suas consoantes maiúsculas; str->str"""
    contador = 0
    acumulador = ''
    while contador< len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyzç':
            acumulador = acumulador + str.upper(frase[contador])
        if frase[contador] not in 'bcdfghjklmnpqrstvwxyzç':
            acumulador = acumulador + frase[contador]
        contador  = contador  + 1
    return acumulador