def conta_frases(texto):
    '''Conta a quantidade de frases em um texto;
    entrada: str;
    saída: int;
    '''
    return str.count(texto, '…') + str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?')