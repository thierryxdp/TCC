# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
      '''antes = str1[:len(str1)//2]
         depois = str1[len(str1)//2:]
         str1 = "#" + antes + "#" + depois + "#"
      '''
    
     str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    
    return str1