def conta_frases (texto) :
    '''Recebe um texto em formato de string e conta a quantidade
    de frases. A função identidica as frases sabendo que o texto
    pode terminar em ponto final, de interrogação, exclamação e 
    reticência, retornando o número de frases (nfrase)'''
    nfrase += texto.count('...')
    nfrase -= texto.count('...')*3
    nfrase = texto.count('!')
    nfrase += texto.count('?')
    nfrase += texto.count('.')

    return nfrase