# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' função que recebe uma string e insere a "#" no inicio, no meio e no fim;
           str-> str'''
    meio= len(s)//2
    return "#" + s[:meio]+ "#" + s[meio:] + "#"