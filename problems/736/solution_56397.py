# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Dadas duas strings a e b, retorna a concatenação delas no formato abba
    assinatura:
    str, str --> str
    testes:
    concatenacao( 'batata', 'frita' ) == 'batatafritafritabatata'
    concatenacao( 'abc', 'def' ) == 'abcdefdefabc'
    concatenacao( 'oi', 'ola' ) == 'oiolaolaoi'
    """
    return a + 2 * b + a