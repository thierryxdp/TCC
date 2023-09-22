def conta_frases(texto):
    '''Função que recebe um texto e retorna a quantidade de frases contidas nele
    levando em conta que a frase é terminada com um ponto final, de exclamação,
    interrogação ou reticências. str -> int'''
    
    return str.count(texto,'!') + str.count(texto,'?')+str.count(texto,'...') + (str.count(texto,'.') - 3*str.count(texto,'...'))