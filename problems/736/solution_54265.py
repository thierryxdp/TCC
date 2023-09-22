# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """recebe duas variáveis e retorna contatenado
    str,str->str"""
    return a + b + a[:-1] + b[:-1]