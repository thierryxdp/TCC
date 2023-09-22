def conta_frases(x):
    """Conta o número de frases a partir da frequência de pontuação"""
    conta_frases = x.split('.', '!', '?')
    
    print conta_frases