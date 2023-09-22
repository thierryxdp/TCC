def conta_frases(texto):
    ''' Função que recebe um texto como entrada e retorna o número de
    frases que aparecem nesse texto. Cada frase é terminada com um ponto final,
    um ponto de exclamação, um ponto de interrogação ou três pontos em sequência
    (reticências).Pontos de exclamação e interrogação não aparecem repetido em
    sequência no texto e esses símbolos só aparecem no texto terminando uma frase
    ;str->int'''
    return str.count(texto,'!')+ str.count(texto,'?')+ str.count(texto,'...')+ (str.count(texto,'.')- 3* str.count(texto,'...'))