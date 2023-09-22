def uppCons(texto):
    i = 0
    letras_maiusc = ''

    while i < len(texto):
        if texto[i] in 'qwrtypsdfghjklçzxcvbnm': 
            letras_maiusc = letras_maiusc + texto[i].upper()
        elif texto[i] in 'QWERTYUOPASDFGHJKLÇZXCVBNMaeiouóáéíóã':
            letras_maiusc=letras_maiusc+texto[i]
        i+=i+1
    return letras_maiusc