# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que retorna uma string com o caractere '#' no inicio, no meio e no final da mesma"""
    x = '#'
    repartida = len(s)//2
    final = x + s[:repartida] + x + s[repartida:] + x
    return final