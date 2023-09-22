# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Retorna a concatenação de a e b, duas strings, no formato
    abba;
    string, string -> string"""
    uniao_strings = a + b
    return uniao_strings + uniao_strings[-1::-1]