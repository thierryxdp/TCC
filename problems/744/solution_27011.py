# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    comprimento = len(s)
    meio = round(comprimento / 2,1)
    meio = int(meio)
    parte_um, parte_dois = s[:meio], s[meio:]
    return '#' + parte_um + '#' + parte_dois + '#'