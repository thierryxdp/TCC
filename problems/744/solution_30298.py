# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que insere o caractere # em uma dada string, no inicio, no meio e no final
    string -> string'''
    caracteres = len(s)
    posicao_meio = caracteres//2
    parte_1 = s[0:posicao_meio]
    parte_2 = s[posicao_meio:]
    return '#'+ parte_1 + '#' + parte_2 + '#'