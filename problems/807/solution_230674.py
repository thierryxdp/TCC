def conta_frases(texto):
    '''Conta a quantidade de frases em um texto;
    entrada: str;
    saída: int;
    '''
    textosemreticencias = str.strip(texto,'...')
    return str.count(texto, '...') + str.count(textosemreticencias,'.') + str.count(texto,'!') + str.count(texto,'?') + str.count(texto, ';')