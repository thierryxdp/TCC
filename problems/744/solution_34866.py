# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(texto):
    '''uma função chamada hashtag que receba uma string e insira o caractere ”#” no início, no meio
e no final dela'''
    # str > str
    i = len(texto)//2
    return '#' + texto[:i] + '#' +texto[i:] + '#'