def contador(conta_frases):
    return len(conta_frases.split('!')) + len(conta_frases.split('?'))+len(conta_frases.split('.')) + len(conta_frases.split('...'))