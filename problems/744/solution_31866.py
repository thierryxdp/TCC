# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Essa funcao recebe uma string e insere o carectere # no inicio e no final da mesma
    str->str'''
     #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1