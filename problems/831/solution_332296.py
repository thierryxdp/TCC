def lingua_p(palavra):
    """Retorne a palavra de entrada traduzida pela língua do P"""
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            list.insert(vogais,i+1,'p')
        if palavra[i] in vogais:
            list.insert(vogais,i+2,palavra[i])
    return vogais