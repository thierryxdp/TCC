# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    funcao que recebe uma string e insere um caractere "#" no 
    inicio, no meio e no final dela
    :param s: str
    :return: str
    '''
    meio = len(s)//2
    return "#" + s[0:meio] + "#" + s[meio:] + "#"