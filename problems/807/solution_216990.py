def conta_frases(texto):
    '''função que retorna a quantidade de frases que existe de entrada, tal que
o separador de cada frase são os pontos: final, exclamação, interrogação e
reticências, tal que quando separados os pontos de exclamação e interregação
não serão repetidos;
string->int'''
    a = str.count(texto,'.')
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')

    return (a+b+c+d)