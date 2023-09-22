# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):   
'''retorna uma string com "#" no início, meio e no final dela;.
str-> str '''

    x = s[0:math.floor(len(s)/2)]
    y = s[math.floor(len(s)/2):len(s)]
return '#' + x + '#' + y + '#'