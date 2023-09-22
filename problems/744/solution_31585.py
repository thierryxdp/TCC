# Funçao que insere o caractere "#" no inicio, meio e fim
# de uma string
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funçao que insere o caractere "#" no inicio, meio
    e fim de uma string'''
    return "#"+s[0:int(len(s)/2)]+"#"+s[int(len(s)/2):]+"#"