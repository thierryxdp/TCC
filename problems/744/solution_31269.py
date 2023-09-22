# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio  =  len ( s ) //2
    nova_string  =  '#'  +  s [: meio ] +  '#'  +  s [ meio :] +  '#'
    return  str(nova_string)