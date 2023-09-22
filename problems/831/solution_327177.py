def lingua_p(palavra:str):
    novapalavra = ''
    for vogal in palavra:
        if vogal == 'a' or 'e' or 'i' or 'o' or 'u':
            novapalavra = '' + 'p' + vogal + palavra
           
            
    return novapalavra