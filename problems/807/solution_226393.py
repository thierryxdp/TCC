def conta_frases(txt):
    '''eu recebo uma string e conto o numero de frases contida nela.
str -> int'''
    quantidade1=str.count(txt,'!')
    quantidade2=str.count(txt,'...')
    quantidade3=str.count(txt,'.')valor2*3
    quantidade4=str.count(txt,'?')
    return (quantidade1+quantidade2+quantidade3+quantidade4)