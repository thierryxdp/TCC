# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'funçao que retorne a str"#" no inicio meio e fim;str-str'
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s