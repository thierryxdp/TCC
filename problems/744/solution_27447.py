# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string 's' e insere o caractere '#' no início, no meio e no fim da string
       valor de entrada:str
       valor de saída:str"""
    return '#'+s[0:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'