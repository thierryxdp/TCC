# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que dada uma string(s-> str) retorna ela com #c inseridos no omeço no meio e no fim [entrada(str)] [saida(str)]'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s