def lingua_p(palavra):
    """ Dado uma palavra, ela retorna na lingua do P"""
    palavra_p = []
    for vogal in ['a','e','i','o','u']:
        palavra_p = str.replace(palavra_p, vogal, 'p')
    return palavra_p