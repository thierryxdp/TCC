# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(str1):
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pré + "#" + pos + "#"
    str1  =  "#"  +  str1 [: len ( str1 ) // 2 ] +  "#"  +  str1 [ len ( str1 ) // 2 :] +  "#"
    retornar  str1