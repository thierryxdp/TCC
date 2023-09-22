# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio=(len(s)//2)
    parte1=s[0:meio]
    parte2=s[meio:len(s)]
    return '#'+ parte1 + '#' + parte2 + '#'