# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcao que recebe uma string e insere o caractere '#' no início, no
meio e no final dela; str -> str"""
    x = '#'
    y = len(s)//2
    return x + s[0:y] + x + s[y:] + x