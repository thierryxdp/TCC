def lingua_p(palavra):
    '''Função que altera a palvra original ao traduzir-la para a lingua do P,
    conforme adiciona, após cada vogal orignal da palavra, uma
    consoante 'p' junto da vogal correspondente
    str -> str'''
    palavra = palavra.lower()
    adiciona = ''
    for vogal in palavra:
        if vogal in 'aáàâãeéêiíoóôõuú':
            adiciona += vogal + 'p' + vogal
        else:
            adiciona += vogal
    return adiciona