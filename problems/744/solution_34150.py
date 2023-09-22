# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que coloca '#' no meio da string
assinatura: str -> str
"""
    pri=s[1:2:1]
    seg=s[len(s)/2::1]
    has='#'
    return has+pri+has+seg+has