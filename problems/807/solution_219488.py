# Retorna o número de frases de um texto, dividindo por pontuação.
# str -> int
def conta_frases(t):
    return t.split(' ') - (t.count('.') + t.count('?') + t.count('!') + t.count('...'))