def conta_frases(string):
    """Dada uma string retorna o número de frases;
    string -> int"""
    p_exclamacao = string.count('!')
    p_interrogacao = string.count('?')
    reticencias = string.count('...')
    p_final = string.count('.') - 3*reticencias
        
    return p_final+p_exclamacao+p_interrogacao+reticencias