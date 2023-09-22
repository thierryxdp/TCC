# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a = int (len(s)/2)
    b = s[0:a]
    c = s[a:]
    
    if len(s) == 1:
        return "##" + str(s) + "#"
    else:
        return "#" + str(b) + "#" + str(c) "#"