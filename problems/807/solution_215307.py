def conta_frases(frase):
    """Função que determina a quantidade de frases em 
    um texto, a partir da puntuação: '.', '...', '?' e '!';
    str -> int"""
    ponto_final = frase.count('.')
    reticencias = frase.count('...') 
    interrogacao = str.count(frase,'?')
    exclamacao = str.count(frase,'!')
    
    return  ponto_final + reticencias + interrogacao + exclamacao