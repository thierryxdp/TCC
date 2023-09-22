def lingua_p(palavra):
    """Retorne a palavra de entrada traduzida pela língua do P"""
    vogais = ('a','e','i','o','u','A','E','I','O','U')
    nova =()
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            list.insert(nova,i+1,palavra[i])
        list.insert(nova,i+1,'p')
    return nova