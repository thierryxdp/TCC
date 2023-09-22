def conta_frases(x):
    """ Dado um texto retorna quantidade de frases existentes. string -> int"""
    reticencias = x.count('...')
    final = x.count('.')
    exclamacao = x.count('!')
    interrogacao = x.count('?')
    return final - (2*reticencias) + exclamacao + interrogacao