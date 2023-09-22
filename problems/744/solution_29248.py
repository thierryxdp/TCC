# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s,hashtag='#'):
    """Retorna a string s, porém, adiciona-se # no inicio, meio e final dela;
string;String->string"""
    i=len(s)//2
    return hashtag+s[0:i]+hashtag+s[i:]+hashtag