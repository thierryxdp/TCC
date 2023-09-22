def uppCons(texto):
    i = 0
    letras_maiusc = ''

    while i < len(texto):
        if texto[i] in 'qwrtypsdfghjklçzxcvbnm': 
            letras_maiusc = letras_maiusc + texto[i].upper()
        i += 1
        else:
            letras_maiusc=text[i]
    return letras_maiusc