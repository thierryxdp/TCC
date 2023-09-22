def conta_frases(texto):
    '''Função que recebe um texto e retorna a quantidade de frases que o texto possui'''
    return str.count(texto,".") + str.count(texto,"!") + str.count(texto,"?") - 2*str.count(texto,"...")