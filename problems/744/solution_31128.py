# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string s, porém com a adição de hashtags no
    início, meio e fim da string
    str -> str"""
    if (len(s)%2==0):
        metade1=len(s)/2
    else:
        metade1=len(s)//2
    return str('#'+str(s[: int(metade1)])+'#'+str(s[int(metade1):])+'#')