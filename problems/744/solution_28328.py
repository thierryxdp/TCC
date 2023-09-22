# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """funcao querecebe uma str 's' e retorna # no inicio
    no meio e no final da str 's':ex. '#ab#cd#'   entrada
    str,saida str"""
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'