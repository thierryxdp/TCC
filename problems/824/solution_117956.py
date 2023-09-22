def uppCons(texto):
    i = 0
    letras_maiusc = ''

    while i < len(texto):
        if texto[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZX': 
            letras_maiusc = letras_maiusc + texto[i]
        i += 1
    return letras_maiusc