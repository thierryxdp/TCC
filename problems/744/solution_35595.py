# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   s=str
 um = str [:len(str)//2]
   dois = str[len(str)//2:]
   str = "#" + um + "#" + dois + "#"
   str = "#" + str[:len(str)//2] + "#" + str[len(str)//2:] + "#"
    return str