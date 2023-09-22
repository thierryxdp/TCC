def conta_frases(texto):
    return len(re.split('[?.!...]', texto))