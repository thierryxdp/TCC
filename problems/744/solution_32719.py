# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)//2
    inicio = s[0:x]
    final = s[x+1:len(s)]
    return str('#')+str(inicio)+str('#')+str(final)+str('#')