def uppCons(frase):
    cons_up = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] in 'bcçdfghjklmpqrstvwxyz':
            cons_up += frase[indice].upper()
    return cons_up