# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "retorna # no inicio, no meio e no final da string s"
    met = len(s)//2
    return '#' + s[:met] + '#' + s[met:len(s)] + '#'