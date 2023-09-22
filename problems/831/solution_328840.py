def lingua_p(palavra):
    '''Função que recebe um palavra e a traduz para a Língua
    P, essa tradução se dá quando após uma vogal da palavra original
    é inserida a letra 'p' mais a vogal.
    str -> str'''
    palavra = str.lower(palavra)
    palavra_traduzia = ''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
        	palavra_traduzida = palavra[:i] + 'p' + palavra[i] + palavra[i:]
    return palavra_traduzida