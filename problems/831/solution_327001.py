def lingua_p(palavra):
    x=str.lower(palavra)
    c = 0
    palavra_nova = ''
    for carac in palavra:
        if carac in 'aeiouáéíóúâîãà':
            palavra_nova += carac + 'p' + carac
        else:
            palavra_nova += caractere
    return palavra_nova