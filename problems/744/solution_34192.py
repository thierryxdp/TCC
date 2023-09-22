# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """A função recebe uma string e adiciona o caractere # no inicio, no meio e no final dela
Casos de Teste
'abcd'==#ab#cd#
'efghi'==#ab#ghi#
"""
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1