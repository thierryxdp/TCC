def uppCons(frase):
    #Dado uma frase, retorna ela com todas consoantes em maiúsculas. str -> str
    proximo = 0
    nova_frase = ''
    vogais = ['a','á','à','ã','e','é','ê','i','í','î','o','ô','ó','õ','u','û','ú']
    while proximo < len(frase):
        if frase[proximo] in vogais:
            nova_frase += frase[proximo]
        else:
            nova_frase += frase[proximo].upper()
        proximo = proximo + 1
    return nova_frase