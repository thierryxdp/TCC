def uppCons(texto):
    i = 0
    letras_maiusc = ''

    while i < len(texto):
        if texto[i] in 'qwrtypsdfghjklçzxcvbnm': 
            letras_maiusc = letras_maiusc + texto[i].upper()
        else:
            letras_maiusc = letras_maiusc+text[i]
        i=i+1
    return letras_maiusc