# Retorna o número de frases de um texto, dividindo por pontuação.
# str -> int
def conta_frases(t):
    return len(t.split('.').split('!').split('?').split('...'))