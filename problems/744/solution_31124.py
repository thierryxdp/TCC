# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    salvo = len(s)//2
    nova = "#"+s[0:salvo]+"#"+s[salvo:]+"#"