# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    comprimento = len(s)
    compr = len(s)//2
    parte1 = s[0:compr]
    parte2 = s[compr:comprimento]
    return '#'+ parte1 + '#' + parte2 + '#'