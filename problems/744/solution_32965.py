# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''uma função que insere '#' no início, no meio e no final dela. exemplo: "abcd" vira "#ab#cd#"
    str-> str'''
    meio = len(s)//2
    return '#'+s[0:meio]+'#'+s[meio:]+'#'