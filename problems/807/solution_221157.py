def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    if '...' in texto:
        ponto_final = str.count(texto,'.') - 2 *str.count(texto,'...') 
        numero_frases = str.count(texto,'!') + str.count(texto,'?') + ponto_final
        return numero_frases
    else:
        numero_frases = str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')
        return numero_frases