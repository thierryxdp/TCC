def conta_frases(frases):
    return len(str.partition(frases,'...'))+len(str.partition(frases,'!'))+len(str.partition(frases,'?'))+len(str.partition(frases,'.'))-2