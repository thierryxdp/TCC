# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ recebe e retorna uma string s inserindo  # no inicio, no meio e no final"""
    meio=int(len(s)/2)
    inicio=str(s[:meio])
    final=str(s[meio:])
    return str('#' + inicio + '#' + final + '#")