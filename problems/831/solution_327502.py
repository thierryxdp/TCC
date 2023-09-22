def lingua_p(palavra):
    """retorna a palavra dada traduzida para a língua do P."""
    palavra=str.lower(palavra)
    palavra=list(palavra)
    n=0
    while n<len(palavra):
        l=palavra[n]
        if l not in 'bcdfghjklmnpqrstvwxyz':
            list.insert(palavra,n+1,'p'+palavra[n])
            n+2
        else:
            n=n+1         
    return str.join('',palavra)