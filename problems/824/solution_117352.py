def uppCons(frase):
    cons_up = ''
    indice = 0
    while indice < len(frase):
        if frase[indice] == 'bcdfghjklmpqrstvwxyz':
            cons_up = str.replace(frase,frase[indice],str.upper(frase[indice]))
        indice += 1
    return cons_up