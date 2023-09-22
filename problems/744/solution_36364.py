# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Função recebe uma string. Acrescenta um # antes, outro no meio e outro no final.
    Retorna uma string
    '''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s