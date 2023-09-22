def conta_frases(texto):
    '''Conta a quantidade de frases em um texto;
    entrada: str;
    saída: int;
    '''
    if '...' in texto:
        textosemreticencias =str.strip(texto, '...')
    else:
        textosemreticencias = texto
    return str.count(texto, '...') + str.count(textosemreticencias,'.') + str.count(texto,'!') + str.count(texto,'?')