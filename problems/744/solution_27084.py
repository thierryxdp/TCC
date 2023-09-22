# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no inicio, meio e fo=inal do string
       Entrada: str
       Saida: str
    """
    if 2 <= len(s) <= 3:
        return # + s[0:1] + # + s[1:] + #