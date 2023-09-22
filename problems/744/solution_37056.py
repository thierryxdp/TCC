# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'retorna uma string com # no incio,meio e fim'
    'string->string
    partes=len(s)//2
    return '#'+s[:partes]+'#'+s[:partes]+'#'