# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(abcde):
    """ Insere uma # no início, meio e fim da string.
entrada: str
saída:str
"""
    return '#' + (abcde[ :len(abcde)//2]) +'#' + (abcde[len(abcde)//2: ]) +'#'