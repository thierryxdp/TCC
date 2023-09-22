# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna uma string adicionando # no início, meio e
    final dela;
    str -> str"""
    i= len(s)/2
    h = '#'+ s[:i] + '#'+ s[i:] + '#'
    return h