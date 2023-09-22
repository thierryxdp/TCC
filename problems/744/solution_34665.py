# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Funçao que recebe uma string e insere o caractere(#)
    no inicio, no meio e no final dela
    str->str'''
    mid=len(s)/2
    h=str('#')
    return h+s[0:mid]+h+s[mid+1:]+h