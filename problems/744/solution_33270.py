# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s:str):
    """Função que recebe uma string e insere "#" no inicio,meio e final da string"""
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'