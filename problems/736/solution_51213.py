# Função que concatena os textos a, b em abba
# a: texto qualquer; b: texto qualquer
# str, str -> str
def concatenacao(a, b):
    def concatenação (a:str, b:str) -> str:
    c = b[::-1]
    d = a[::-1]

    return a + b + c + d