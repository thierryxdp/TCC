def conta_frases(texto):
    '''
    funcao que recebe um texto em string e retorna
    o numero de frases desse texto
    string->int
    '''
    exclamacao=texto.replace('!','.')
    interrogacao=exclamacao.replace('?','.')
    reticencias=interrogacao.replace('...','.')
    textofinal=reticencias
    return str.count(textofinal,'.')