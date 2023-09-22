# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    total = len(s)//2 
    parte1 = s[:total]
    parte2 = s[total:]
    return str('#') + str(parte1)+ str('#') + str(parte2) + str('#')