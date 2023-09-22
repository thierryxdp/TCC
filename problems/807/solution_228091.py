def conta_frases(sentenca):
    '''função que retorna o número de frases de uma dada sentença
    string -> int'''
    s1 = sentenca.replace('!', 'x')
    s2 = s1.replace('.', 'x')
    s3 = s2.replace('?', 'x')
    s4 = s3.replace('...', 'x')
    s5 = s4.replace('xxx', 'x')
    return len((s5.split('x')))