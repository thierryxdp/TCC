# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '1'+str(s[0:int(len(s)//2)])+'1'+ str(s[int(len(s)//2):int(len(s))])+'1'