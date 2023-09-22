# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """ Retorna as strings a e b na ordem a->b->b->a
    testes:
    concatenacao('cozinhar','arroz')= 'cozinhararrozarrozcozinhar'
    concatenacao('ele','ela') = eleelaelaele"""
    return a + b + b + a