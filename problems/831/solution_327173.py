def lingua_p(palavra:str):
    novapalavra = ''
    for vogal in palavra:
        if vogal == 'a':
            novapalavra = '' + vogal + 'p' + palavra
        if vogal == 'e':
            novapalavra = '' + vogal + 'p' + palavra
        if vogal == 'i':
            novapalavra = '' + vogal + 'p' + palavra
        if vogal == 'o':
            novapalavra = '' + vogal + 'p' + palavra
        if vogal == 'u':
            novapalavra = '' + vogal + 'p' + palavra
            
    return novapalavra