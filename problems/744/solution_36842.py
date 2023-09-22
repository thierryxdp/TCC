# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ insere o caractere (#) no início,
    no meio e no final da string recebida.
assinatura:str
"""
    return "#" + str(s[:(len (s)//2)]) + "#" + str(s[(len(s)//2):]) + "#"