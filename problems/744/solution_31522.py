# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''
    Função que recebe uma string e após isso insere 3 caracteres # no início,
    no meio e no final da string.
    Param s: str
    Return: str
    '''
    meio = len(s)//2
    return ('#' + s[:meio] + '#' + s[meio:] + '#')