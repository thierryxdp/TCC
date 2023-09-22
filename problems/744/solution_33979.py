# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    '''funcao que acrescenta uma hastag no inicio, meio  fim de uma string;
    str -> str'''
     return '#' + x[:len(x)//2] + '#' + x[len(x)//2:] + '#'