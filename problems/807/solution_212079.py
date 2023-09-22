def conta_frases (texto):
    """Função que conta o número de frases, dado um texto de entrada
    Entrada: String
    Saída: Int"""
    
    qnt_pontos = str.count(texto, '.')
    qnt_reticencias = str.count(texto, '...')-3*str.count(texto,'...')
    qnt_exclamacao = str.count(texto, '!')
    qnt_interrogacao = str.count(texto, '?')
    
    return qnt_pontos + qnt_reticencias + qnt_exclamacao + qnt_interrogacao