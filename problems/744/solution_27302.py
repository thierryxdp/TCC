# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que recebe uma string e retorna o caractere # no início,meio e
no fim da string
Entrada(str)
Saída(str)'''
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'