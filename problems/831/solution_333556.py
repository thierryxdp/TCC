def lingua_p(texto):
    '''recebe uma string e retorna uma nova string com a tradução para a língua P proposta no exercício
    str -> str
    '''
    novotexto=''
    for vogal in texto:
        if vogal in 'AEIOUaeiouáéíóú':
            novotexto += vogal + 'p' + vogal
        else:
            novotexto += vogal
    return novotexto