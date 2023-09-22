def lingua_p(palavra):
    """ Função que recebe como parâmetro uma palavra e retorna
        esta mesma palavra traduzida para a língua do P, ou seja,
        após cada vogal da palavra original, é inserida a sequência
        de letras 'p' mais a vogal original
        string -> string"""
    palavra_minuscula = str.lower(palavra)
    palavra_traduzida = ''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            palavra_traduzida = palavra_traduzida + letra +'p' + letra
        else:
            palavra_traduzida = palavra_traduzida + letra
    return palavra_traduzida