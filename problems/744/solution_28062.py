# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """insere um caractere # no inicio, meio e final de um dado string
    parametros: s -> str
    retorna str"""
    
    return '#' + s[0: len(s)//2] + '#' + s[len(s)//2:] + '#'