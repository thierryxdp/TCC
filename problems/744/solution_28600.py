# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna, dado uma string, a string informada
    com o símbolo '#' em seu início, meio e fim.
    str->str"""
    if len(s) == 1:
        return str('#') + str('#') + s + str('#')
    else:
        return str('#') + s[0:len(s)//2] + str('#') + s[len(s)//2:] + str('#')