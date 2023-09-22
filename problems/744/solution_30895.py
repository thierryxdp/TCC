# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    strin = s
    s1 = strin[:len(strin)//2]
    s2 = strin[len(strin)//2:]
    return "#"+s1+"#"+s2+"#"