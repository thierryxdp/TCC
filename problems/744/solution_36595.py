# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna a string com o caractere # no início, meio e fim
    entrada: string
    saída: string
    '''
    i = len(s) // 2
    s = "#" + s[0:i] + "#" + s[i:] + "#"
    return s