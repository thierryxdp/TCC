# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' função que dado uma str(s) deve retornar o caractere "#" no ínicio, meio e fim desta string.'''
    meio = len(s)//2
    return "#" + s[:meio] + "#" + s[meio:] + "#"