# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Dadas duas strings 'a' e 'b', a função retorna uma concatenação das duas strings no formato 'abba';
    str --> str"""
    concat = str(a)+str(b)+str(b)+str(a)
    return concat