def lingua_p(frase):
    """ esta função recebe uma palavra como parametro e retorna a mesma traduzida
    para a lingua do p, isso significa inserir depos cada vogal a letra p e
    a sequencia de p mais a vogal."""
    vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ''
    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra
        elif letra in vogaisup:
            palavra = palavra +  letra + 'p' + letra
        else:
            palavra = palavra + letra
    return str.lower(palavra)