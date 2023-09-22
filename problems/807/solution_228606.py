def conta_frases(texto):
    for k in ['.','...','!','?']:
        x=str.partition(texto,k)
    return x