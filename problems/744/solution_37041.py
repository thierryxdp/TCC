#Função que coloca # no ínicio, meio e final de uma string. Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s