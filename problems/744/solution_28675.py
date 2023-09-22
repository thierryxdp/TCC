# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Insere a string "#" no innício, no meio e no final da string
    str -> str"""
    meio = len(s) // 2 # Define o meio da string
    return "#" + s[0:meio] + "#" + s[meio:len(s)] + "#"