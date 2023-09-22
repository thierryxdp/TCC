# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''através da concatenação e a obtenção do tamanho da string
    é calculado a posição do meio para que se possa ser substituído
    pela hastag, a outra sendo colocada na posição final'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s