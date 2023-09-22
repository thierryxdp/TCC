# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

def hashtag(s):
    from math import floor
    meio = floor(len(s)/2)
    return "#"+s[:meio]+"#"+s[meio:]+"#"