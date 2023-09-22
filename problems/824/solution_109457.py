def uppCons (frase):
    frase_consoante = ''
    c = 0
    while c < len (frase):
        if not frase [c] in 'aeiouAEIOU' and frase [c].isalpha() or frase [c] == 'ç':
            frase_consoante += frase [c].upper()
        else:
            frase_consoante += frase [c]
        c += 1
        
    return frase_consoante