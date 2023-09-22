# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''a função coloca # no inicio , meio e fim da string (s) (str->str)'''
    return "#"+s[:int(len(s)/2)]+"#"+s[int(len(s)/2):]+"#"