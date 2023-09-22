# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string s de entrada com o símbolo # em seu início, meio e fim"""
    """str -> str"""
    a=len(s)//2
    return ''.join('#',s[0:a],'#',s[a:],'#')