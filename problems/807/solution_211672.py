def conta_frases(texto):
    '''Conta o número de frases presentes no texto dado;
    str -> int'''
    n'.'=str.count(texto[1],'.')
    n'...'=str.count(texto[1],'...')
    n'?'=str.count(texto[1],'?')
    n'!'=str.count(texto[1],'!')
    return n'!'+n'?'+n'.'-2*n'...'