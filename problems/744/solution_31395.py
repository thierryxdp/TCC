# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e coloca o simbolo"#" no inicio no 
    meio e no final da string"'''
    tam=len(s)
    i=tam//2
    return '#' + s[0:i] + '#' + s[i:] + '#'