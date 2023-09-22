# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "Funcao que retorna o #, no inicio, no meio dele mesmo e no final"
    return '#' + s[:len(s)/2] + '#' + s[len(s)/2:] + '#'