# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio=len(s)//2
    s2=str.join("#",(s[0:meio],s[meio:]))
    s1='#'
    return s1+s2+s1