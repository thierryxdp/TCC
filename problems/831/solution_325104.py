def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    for letra in string:
        if letra in 'aeiouAEIOU':
            novastring=str.replace(string,'letra','letrap')
        return novastring