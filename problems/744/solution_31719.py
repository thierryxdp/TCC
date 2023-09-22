# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i = int(len(s)/2)
    s1 = s[:i]
    s2 = s[i+1:]
    return "#"+s1+"#"+s2+"#"