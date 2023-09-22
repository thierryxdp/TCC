# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    '''concatena duas str entre si e a essa sema sera concatenada
    a inversao dela mesma
    entrada: str, str
    saida: str'''
    soma = a + b
    invertido = b + a
    return soma + invertido