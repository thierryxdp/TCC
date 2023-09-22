def conta_frases(frase):
    '''função que conta o número de frases dado um texto. Cada frase no texto é
    terminada com um ponto final, um ponto de exclamaç˜ao, um ponto de interrogação
    ou três pontos em sequência(reticências). exclamaç˜ao ou interrogaç˜ao
    n˜ao aparecer˜ao repetidos em sequência no texto e esses símbolos só aparecem
    no texto terminando uma frase.
    str->int. '''
    interrogacao=str.count(frase,'?')
    exclamacao=str.count(frase,'!')
    reticencias=str.count(frase,'...')
    ponto=str.count(frase,'.')
    x=ponto-reticencias*3
    return interrogacao+exclamacao+reticencias+x