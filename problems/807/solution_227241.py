def conta_frases(frases):
    '''função que conta o número de frases que aparecem em um dado texto,sendo cada frase terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência (reticências); string -> int'''
    frase=0
    '.'!='...'
    if '.' in frases:
     frase+=(str.count(frases,'.'))
    if '!' in frases:
     frase+=(str.count(frases,'!'))
    if '?' in frases:
     frase+=(str.count(frases,'?'))
    if '...' in frases:
     frase+=(str.count(frases,'...'))-(3*(str.count(frases,'...')))
     return frase
    else:
        return frase