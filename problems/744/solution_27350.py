# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe e retorna uma string s inserindo o caractere # no início, no
    meio e no final dela"""
    meio=int(len(s)/2)
    inicio=str(s[:meio])
    final=str(s[meio:])
    return str('#' + inicio + '#' + final + '#')