# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string e adiciona "#" no início, meio e fim da mesma
    assinatura: str -> str
    testes: hashtag ("drogaria") == '#drog#aria#'
    hashtag ("bit") == '#b#it#'
    """
    return '#' + str [s :len (s) / 2] + '#' + str (s [0:2] ) + '#'