# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    tam_s = s.len()
    i = tam_s/2
    return "#" + s[:i] + "#" + s[i:] + "#"