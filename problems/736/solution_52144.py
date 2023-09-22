# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Função que dadas duas strings retorna a concatenação delas 
    str, str --> str"""
    c1 = a+b
    inverte = c1[::-1]
    return inverte