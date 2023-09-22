# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    '''Recebe uma string e insere o caractere '#' no início, no meio e no
    final dela (ex: "abcde" -> "#ab#cde#")
    str ->str'''

    primeiraMetade = string[:len(string)//2]
    segundaMetade = string[len(string)//2:]

    return '#' + primeiraMetade + '#' + segundaMetade + '#'