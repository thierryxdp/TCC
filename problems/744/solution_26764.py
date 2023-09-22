# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Dada uma string 's', a função retorna essa mesma string com o caractere '#' inserido no início, no meio e no final dessa string;
    str --> str"""
    a = (len(s))//2
    b = '#'+s[0:a]+'#'+s[a:]+'#'
    return b