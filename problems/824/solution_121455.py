def uppCons(frase):
    nova_frase = ''
    e = 0
    tamanho_frase = len(frase)
    consoantes = 'bcdfghjklmnpqrstvxwyz'
    while e < tamanho_frase:
        if frase[e] in consoantes:
            nova_frase = nova_frase + frase[e].upper()
        else:
            nova_frase = nova_frase + frase[e]

        e = e + 1
    return nova_frase