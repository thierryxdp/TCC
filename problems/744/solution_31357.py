# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ dado ums string s retorna uma nova string com o
    caractere '#' no inicio, no meio e no fim dela
    str -> str"""
    palavra = s
    tamanho = len(palavra)
    metade = int(tamanho/2)
    meio = palavra[:metade]
    final = palavra[metade:]
    return '#' + meio + '#' + final + '#'