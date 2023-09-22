def conta_frases(f):
    """Função em que dada uma fala escrita segundo as regras da Língua Potuguesa conta o número de frases presente
    string -> int"""
    return f.count('.')-(2*f.count('...'))+f.count('!')+f.count('?')