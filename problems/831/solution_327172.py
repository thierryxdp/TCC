def lingua_p(palavra:str):
    novapalavra = ''
    for vogal in palavra:
        if vogal == 'a':
            novapalavra = '' + 'p' + vogal + palavra
        if vogal == 'e':
            novapalavra = '' + 'p' + vogal + palavra
        if vogal == 'i':
            novapalavra = '' + 'p' + vogal + palavra
        if vogal == 'o':
            novapalavra = '' + 'p' + vogal + palavra
        if vogal == 'u':
            novapalavra = '' + 'p' + vogal + palavra
            
    return novapalavra