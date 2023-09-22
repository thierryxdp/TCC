# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string com # no início, meio e fim da string
       str->str"""
    s=str(s)
    x=len(s)
    return #+s[0:x//2]+#+s[x//2:]+#