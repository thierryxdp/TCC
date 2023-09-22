# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Entra com uma string e retorna o caractere '#'
    no início, no meio e no final dela
    string->string"""
    corte=len(s)//2
    nova_string='#'+s[:corte]+'#'+s[corte:]+'#'
    return nova_string