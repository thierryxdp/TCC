# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    " Função que faz o fatiamento da String e acrescenta um caractere str---> str"  
   return "#" + s[0:len(s)//2]+ "#" + s[len(s)//2:] + "#"