def lingua_p(palavra):
    '''funç˜ao que recebe como parâmetro uma palavra (em português) e retorne
       esta mesma palavra traduzida para a língua do P. Após cada vogal da palavra
       original é inserida a sequência de letras p mais a vogal original.
       str->str '''
    novaPalavra=''
    contador=0
    vogais=['a','e','i','o','u','A','E','I','O','U']
    consoantes=['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','x','z','y','k']
    for letra in palavra:
        if letra in vogais and letra not in consoantes:
            contador=contador+1
            novaPalavra=letra+'p'+letra
    return str.lower(novaPalavra)