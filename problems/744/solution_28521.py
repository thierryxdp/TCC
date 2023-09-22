# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'função que recebe uma entrada e insira hashtag no principio , no meio e no final'
    pre = s[:len(s)//2]
    pos = s[len(s)//2:]
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s