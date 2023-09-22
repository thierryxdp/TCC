# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ funcao que recebe uma string e insere o caractere '#' no inicio,no meio e no final dela;str,str->"""
    return "#" +  str(s)[:((len(s))//2)] + "#" + str(s)[((len(s))//2):] + "#"