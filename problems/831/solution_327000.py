def lingua_p(palavra):
    x=str.lower(palavra)
    c = 0
    palavra_nova = ''
    for carac in palavra:
        if carac in 'aeiouáéíóúâêîôûãàòù':
            palavra_nova += carac + 'p' + carac
    return palavra_nova