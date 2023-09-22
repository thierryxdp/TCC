# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Dadas duas strings 'a' e 'b', a função retorna a concatenação 
    delas no formato abba.
    str, str --> str
    testes:
    concatenacao('1', '2') == '1221'
    concatenacao('oi', 'tchau') == 'oitchautchauoi'
    """
    return str(a) + str(b) + str(b) + str(a)