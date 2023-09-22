def lingua_p(palavra): 
    ''' Dada uma palavra ela é traduzida para língua do p. str_>str'''
    nova = '' 
    V = 'aáãàeéêèíiìîóòôõouúùû'
    for letra in palavra: 
        if str.lower(letra) in V: 
            nova += str.lower(letra+'p'+ V[str.find(V, str.lower(letra))]
        else: 
            nova += str.lower(letra)
    return nova