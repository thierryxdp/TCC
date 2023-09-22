def lingua_p(texto):
    '''recebe uma string e retorna uma nova string com a tradução para a língua P proposta no exercício
    str -> str
    '''
    novotexto=''
    i = 0
    while (i < len(texto)):
        vogal = texto[i]
        if vogal in 'AEIOUaeiouáéíóú':
            novotexto += vogal + 'p' + vogal
        else:
            novotexto += vogal
        i += 1
    return novotexto