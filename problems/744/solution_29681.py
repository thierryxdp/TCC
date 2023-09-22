# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que dada uma string s como valor de entrada
       retorna caracteres '#' no inicio , meio e fim da string
    str->str'''
    return '#'+ s[0:((len(s)//2))] + '#'+s[((len(s)//2)):len(s)+1]+ '#'