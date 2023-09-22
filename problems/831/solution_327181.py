def lingua_p(palavra:str):
    novapalavra = ''
    vogais = ('a', 'e', 'i', 'o', 'u')
    for vogal in palavra:
        if vogal == 'a' or 'e' or 'i' or 'o' or 'u':
            novapalavra = '' + vogal + 'p' + palavra[:in vogais]
           
            
    return novapalavra