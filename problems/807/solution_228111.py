def conta_frases(sentenca):
    '''função que retorna o número de frases de uma dada sentença
    string -> int'''
    sentenca = sentenca.replace('!', 'x')
    sentenca = sentenca.replace('.', 'x')
    sentenca = sentenca.replace('?', 'x')
    sentenca = sentenca.replace('...', 'x')
    sentenca = sentenca.replace('xxx', 'x')
    return len((sentenca.split('x ')))