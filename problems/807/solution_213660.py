def conta_frases(x):
    reticencias = x.count('...')
    final = x.count('.')
    exclamacao = x.count('!')
    interrogacao = x.count('?')
    return final - (2*reticencias) + exclamacao + interrogacao