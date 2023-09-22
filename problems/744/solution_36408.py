# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = math.floor(len(s)/2)
    s = list(s)
    s = s.insert(0,"#")
    s = s.insert(meio,"#")
    s = s.append("#")
    return s