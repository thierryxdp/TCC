def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases 
    presentes no texto; str-->int'''
    inte=texto.count('?') 
    excl= texto.count('!')
    ponto= texto.count('.')
    reti= texto.count('...')
    reti2= texto.count('...')*3
    return (inte+excl+ponto+reti)-(reti2*3)