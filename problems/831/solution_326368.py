def lingua_p(palavra):
    
    palavra = str.lower(palavra)
    
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    
    papalapavrapa = ''
    
    for i in palavra:
        if i in consoantes:
            papalapavrapa += i
        else:
            papalapavrapa += 'p' + i
    
    return papalapavrapa