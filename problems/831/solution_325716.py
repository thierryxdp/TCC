def lingua_p(palavra):
    '''funç˜ao que recebe como parâmetro uma palavra (em português) e retorne
       esta mesma palavra traduzida para a língua do P. Após cada vogal da palavra
       original é inserida a sequência de letras p mais a vogal original.
       str->str '''
    novaPalavra=''
    for letra in range(len(palavra)):
        if palavra[letra] in 'bcdfghjlmnpqrstvxzykBCDFGHJLMNPQRSTVXZYK':
            novaPalavra=novaPalavra+palavra[letra]
        else:
            novaPalavra=novaPalavra+palavra[letra]+'p'+palavra[letra]
    return novaPalavra