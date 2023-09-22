def conta_frases(texto):
    return (len(str.count('texto','.'))+len(str.count('texto','...'))+len(str.count('texto','?'))+len(str.count('texto','!')))