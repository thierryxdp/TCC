# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(str1):
    '''hashtag no começo meio e fim da string
    ex: ('abcd'), retorna = #ab#cd#'''
#primeiro fazemos a divisão do comprimento da string em 2 partes e depois inserimos a hashtag
    pre = str1[:len(str1)//2]
    pos = str1[len(str1)//2:]
    str1 = "#" + pre + "#" + pos + "#"
    return str1