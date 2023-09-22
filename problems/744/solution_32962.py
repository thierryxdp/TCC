# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma str e insere o caractere # no inicio, meio e fim da str
    entrada: str; saida: str'''
    strlength = len(s)
    strp1 = s[:strlength//2]
    strp2 = s[(strlength//2)+1:]
    return '#' + strp1 + '#' + strp2 + '#'