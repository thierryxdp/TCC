def conta_frases(frase):
    """Função que determina a quantidade de frases em 
    um texto, a partir da puntuação: '.', '...', '?' e '!';
    str -> int"""
    ponto_final = str.count(frase, '.')
    reticencias = str.count(frase, '...') 
    interrogacao = str.count(frase,'?')
    exclamacao = str.count(frase,'!')
    return  reticencias