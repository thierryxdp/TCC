def conta_frases(string):
    '''Função que recebe uma string dada como entrada e retorna o número de frases
    presentes nela. Cada frase no texto  ́e terminada com um ponto final, um ponto
    de exclamação, um ponto de interrogação ou três pontos em sequência.Pontos de 
    exclamação ou de interrogação não aparecerão repetidos em sequência no texto e
    esses símbolos só aparecem no texto terminando uma frase. str->int'''
    x=len(string.split('.','...','!','?'))
    return x