def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases 
    presentes no texto; str-->int'''
    s=texto.count('?' and '!')
    ponto= texto.count('.')
    reti= texto.count('...')
    reti2= texto.count('...')*3
    return (s+ponto+reti)-(reti2*3)