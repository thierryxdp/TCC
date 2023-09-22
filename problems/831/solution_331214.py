def lingua_p(palavra):
    '''Dada uma palavra, a função a traduzirá para
    a lingua "P", onde depois de cada vogal,
    será acrescido P e depois repetirá vogal na 
    frente.'''
    menor=str.lower(palavra)
    letras=list(menor)
    traduz=""
    for consoante in letras:
        if consoante not in "zxcvbnmsdfghjklqwrtyp":
            traduz=traduz+consoante+"p"+consoante
        else:
            traduz=traduz+consoante
    return traduz