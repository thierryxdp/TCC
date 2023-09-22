# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que recebe uma string s retorna o caractere '#' no início, no meio e no final dela.
    entrada: string
    saída string'''
    return '#' + str(s[0:(len(s)//2)]) + '#' + str(s[(len(s)//2)+1:len(s)]) + '#'