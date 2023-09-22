def conta_frases(Texto):
    '''Função que conta o número de frases que aparecem em um texto.
    Parâmetros de Entrada: Str
    Valor de Saída: Int'''
    
    Frases = str.split(Texto,'!') or str.split(Texto,'?') or str.split(Texto,'.') or str.split(Texto,'...')
    
    return len(Frases)