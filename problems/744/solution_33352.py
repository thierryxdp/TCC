# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    ajk
    '''
    caract_s = len(s)
    meio = caract_s//2
    meio1 = s[0:meio]
    meio2 = s[meio:caract_s]
    return '#' + meio1 + '#' + meio2 + '#'