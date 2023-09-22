# Recebe duas strings, a e b e retorna a sua concatenação no formato abba
# str, str -> str
def concatenacao(a, b):
    c = str(a) + str(b) + str(b) + str(a)
    return c