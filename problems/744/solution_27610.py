# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Essa função irá colocar "#" no inicio,meio e final de uma determinada string"""
    h = len(s)//2
    return '#' + s [:h] + '#' + s[h:] + '#'