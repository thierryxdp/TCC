def uppCons(frase):
    """ dada uma frase, função retorna a frase com todas as  consoantes
    maiusculas, mantendo os demais caracteres como estavam na frase
    original. str -> str"""
    s = ''
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s = s + frase[i].upper() 
        else: 
            s = s + frase[i]
        i = i + 1    
    return s