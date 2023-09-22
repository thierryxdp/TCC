def lingua_p(palavra):
    '''Entre com uma palavra para ser retornado a mesma palavra traduzida na
    lingua P
    String -> String'''
    Npalavra=palavra
    x = Npalavra.lower()
    y=len(palavra)
    vogal='aeiou'

    for i in range(len(palavra)):
        if i<y:
            if Npalavra(i) in vogal:
                letra = Npalavra.index(i)
                Npalavra2=Npalavra.insert(i, "p")
                Npalavra3=Npalavra2.insert(i+1, letra)
                
    return Npalavra3