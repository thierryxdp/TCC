def conta_frase(texto):
    '''Funcao que conta o número de frase que
    aparece no texto.
    Dados de entrada: str
    Valor de saida: int 
    '''
    total_frases = str.split(texto,'.'), str.split(texto,'!'), str.split(texto,'?'), str.split(texto,'...')
    return len(total_frases)