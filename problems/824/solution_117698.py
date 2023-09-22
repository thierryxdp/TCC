def uppCons(frase):
    i = 0
    letras_maiusc = ''

    while i < len(frase):
        if frase[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZX':
            letras_maiusc = letras_maiusc + frase[i] 
        i+=1
    return letras_maiusc