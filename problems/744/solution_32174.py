# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funcao que recebe uma string e insira o caractere '#' no inicio, meio
        e fim da mesma. Entrada: str ; Saida: str'''
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'