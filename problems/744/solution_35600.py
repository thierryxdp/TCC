# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    um = str(s) [:len(str)//2]
    dois = str(s)[len(str)//2:]
   s = "#" + um + "#" + dois + "#"