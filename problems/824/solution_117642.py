def uppCons(frase):
    i = 0
    letras_maiusc = ''

    while i < len(frase):
        if frase[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZX':  
            letras_maiusc = letras_maiusc + texto[i] 

    return letras_maiusc