# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Ao receber a string s, retornar a mesma com o caractere '#' no início meio e final  dela"""
    if len(s)%2==0:
        return '#' + s[:(len(s)/2)] + '#' + s[(len(s)/2):] + '#'
    else:
        k= len(s)//2
        return '#' + s[:k] + '#' + s[k:] + '#'