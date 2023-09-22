def conta_frases(texto):
    ponto1= texto.count('!')
    ponto2= texto.count('?')
    ponto3= texto.count('.')
    ponto4= texto.count('...')
    return (ponto1+ponto2+ponto3+ponto4)
'''recebe um texto e calcula o numero de frases contidas nele,string->int'''