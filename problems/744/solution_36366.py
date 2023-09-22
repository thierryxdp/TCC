# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que manipula strings pondo no início,meio e fim um hashtag.
    Assinatura: str->str"""
    n=int(len(s))
    if n%2==0:
        return s[::2]+str("#")