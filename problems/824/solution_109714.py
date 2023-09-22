def uppCons (frase):
    i = 0
    fraseNew = ''
    while i < len(frase):
        consoante = frase [i]
        if consoante in 'bcdfghjklmnpqrstvxwyzç':
            consoante  = str.upper(consoante)
        fraseNew = fraseNew + consoante
        i = i + 1
    return fraseNew