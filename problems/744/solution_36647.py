# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = len(s) // 2 
    stp1 = s.insert('#', meio) 
    return stp1