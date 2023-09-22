# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=str(s)
    meio=len(s)//2
    com=len(s)
    return "#"+s[com:meio:]+"#"