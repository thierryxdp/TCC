def lingua_p(palavra):
    """Retorne a palavra de entrada traduzida pela língua do P"""
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    p =''
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            list.insert(p,i+1,'p')
        if palavra[i] in vogais:
            list.insert(p,i+2,palavra[i])
    return p